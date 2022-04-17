"""Prepare data for Plotly Dash."""
import re
import csv
import pandas as pd
from datetime import datetime, timezone


def erase_file(file_name):
    f = open(file_name, "w+")
    f.close()


def init_output_file():
    file_name = "data/output.csv"
    erase_file(file_name)
    with open(file_name, 'w+') as f:
        f.write('created;constituency_name;party_code;votes')
        f.write("\n")


def init_warnings_file():
    file_name = "data/warnings.csv"
    erase_file(file_name)


def init_parties_file():
    parties_list = [
        {"party_code": "C", "party_name": "Conservative"},
        {"party_code": "L", "party_name": "Labour"},
        {"party_code": "SNP", "party_name": "Scottish National Party"},
        {"party_code": "LD", "party_name": "Liberal Democrats"},
        {"party_code": "G", "party_name": "Green Party"},
        {"party_code": "Ind", "party_name": "Independent"},
    ]

    file_name = "data/parties.csv"
    erase_file(file_name)
    with open(file_name, 'w+') as f:
        f.write('party_code;party_name')
        for party in parties_list:
            f.write("\n")
            party_code = party['party_code']
            party_name = party['party_name']
            f.write(party_code + ';' + party_name)


def init_files():
    init_output_file()
    init_warnings_file()
    init_parties_file()


def check_party_code(party_code):
    file_name = "data/parties.csv"
    file = open(file_name)
    csvreader = csv.reader(file)
    new_party = True
    for row in csvreader:
        row_party_code = re.split("(?<!\\\\);", row[0])[0]
        if row_party_code == party_code:
            new_party = False
    if new_party:
        with open(file_name, 'a') as f:
            f.write("\n")
            f.write(party_code + ';' + party_code)


def transform_csv(input_file_name):
    init_files()

    file = open("data/" + input_file_name, 'r')
    warning_messages = []
    line_count = 0
    while True:
        line_count += 1
        line_str = file.readline()
        if not line_str:
            break
        line = re.split("(?<!\\\\),", line_str)
        constituency_name = line[0]
        line = line[1:]

        pair_num_for_split = 2
        pairs = [line[i:i + pair_num_for_split] for i in range(0, len(line), pair_num_for_split)]
        pair_count = 0

        for pair in pairs:
            pair_count += 1
            try:
                result_error = False
                votes = int(pair[0].strip())
                party_code = str(pair[1].strip())
                if not isinstance(party_code, str):
                    result_error = True
                    warning_messages.append(
                        'error Party name is not string type in line ' + str(line_count) + ' in elem: ' + str(
                            pair_count) + '. Please, check line: ' + line_str)
                if not isinstance(votes, int) or votes < 0:
                    result_error = True
                    warning_messages.append('error votes count is not integer type in line ' + str(line_count) + 'in '
                                                                                                                 'elem: '
                                            + str(pair_count) + '. Please, check line: ' + line_str)
                if not result_error:
                    check_party_code(party_code)
                    with open('data/output.csv', 'a') as f:
                        constituency_name = constituency_name.replace('\,', ',')
                        f.write(str(datetime.now(timezone.utc).strftime(
                            "%Y-%m-%d %H:%M:%S")) + ';' + constituency_name + ';' + party_code + ';' + str(votes))
                        f.write("\n")
            except Exception as e:
                print('error')
                print(e)
                warning_messages.append(
                    'error in line ' + str(line_count) + ' in elem: ' + str(pair_count) + '. Incorrect '
                                                                                          'pair vote '
                                                                                          'and/or '
                                                                                          'party. '
                                                                                          'Please, '
                                                                                          'check line: ')
    for warning_message in warning_messages:
        with open('data/warnings.csv', 'a') as f:
            f.write(warning_message)
            f.write("\n")


def create_dataframe(input_file_name):
    """Create Pandas DataFrame from local CSV."""
    transform_csv(input_file_name)
    df_all_results = pd.read_csv("data/output.csv", parse_dates=["created"], sep=';')
    df_all_results['votes'] = df_all_results['votes'].astype('int')

    total_votes = df_all_results['votes'].sum()

    df_parties = pd.read_csv('data/parties.csv', sep=";")

    df_all_results = df_parties.merge(df_all_results, how='inner', on='party_code')
    df_all_results.rename(columns={'party_name_x': 'party_name'}, inplace=True)

    df_total_votes = df_all_results.groupby(['constituency_name', 'party_name', 'party_code'], as_index=False)[
        'votes'].sum()

    df_total_votes.rename(columns={'votes': 'party_votes'}, inplace=True)

    df_total_votes['max_votes'] = df_total_votes.groupby(['constituency_name'])['party_votes'].transform(max)

    df_total_votes['is_winner'] = df_total_votes['party_votes'] == df_total_votes['max_votes']

    df_total_votes_by_constituency = df_total_votes.groupby(['constituency_name'], as_index=False)['party_votes'].sum()
    df_total_votes_by_constituency.rename(columns={'party_votes': 'constituency_total_votes'}, inplace=True)

    df_electorates = pd.read_csv('data/constituency_uk_2019.csv', sep=";")

    df_total_votes = df_total_votes.merge(df_electorates, how='left', on='constituency_name')
    df_total_votes = df_total_votes.merge(df_total_votes_by_constituency, on='constituency_name')

    df_total_votes['constituency_total_voters'] = df_total_votes['constituency_total_voters'].fillna(0)
    df_total_votes['constituency_total_voters'] = df_total_votes['constituency_total_voters'].astype('int')
    df_total_votes['party_votes'] = df_total_votes['party_votes'].astype('int')
    df_total_votes['constituency_total_votes'] = df_total_votes['constituency_total_votes'].astype('int')
    df_total_votes['votes_turnout_by_party_per_constituency'] = df_total_votes['party_votes'] / df_total_votes[
        'constituency_total_votes']
    df_total_votes['votes_turnout_by_party_over_uk'] = df_total_votes['party_votes'] / total_votes


    df_total_votes['voters_turnout_by_constituency'] = df_total_votes['constituency_total_votes'] / df_total_votes[
        'constituency_total_voters']

    df_total = df_total_votes.groupby(['party_code', 'party_name'], as_index=False)['party_votes'].sum()
    df_total = df_total.sort_values(by=['party_votes'], ascending=False)
    winner_row = df_total.iloc[0]

    df_constituencies = df_total_votes[df_total_votes["is_winner"] == True]
    df_constituencies.rename(columns={'party_code': 'party_winner_code'}, inplace=True)
    df_constituencies.rename(columns={'party_name': 'party_winner_name'}, inplace=True)
    df_constituencies.rename(columns={'party_votes': 'party_winner_votes'}, inplace=True)
    df_constituencies = df_constituencies.sort_values(by=['constituency_name'], ascending=True)
    #df_constituencies = df_constituencies.reset_index()


    parliament_seats = df_constituencies
    parliament_seats.drop(
        ['party_winner_votes', 'max_votes', 'is_winner', 'constituency_total_voters', 'constituency_total_votes',
         'votes_turnout_by_party_per_constituency', 'votes_turnout_by_party_over_uk', 'voters_turnout_by_constituency'],
        axis=1, inplace=True)
    parliament_seats = parliament_seats.groupby(['party_winner_name']).size().reset_index(name='counts')

    parliament_seats = parliament_seats.sort_values(by=['counts'], ascending=False)

    return df_all_results, df_total, df_constituencies, parliament_seats, df_total_votes, winner_row
