html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body class="dash-template">
                            <header>
                              <div class="nav-wrapper">
                                <a href="/">
                                    <img src="/static/img/logo.png" class="logo" />
                                    <h1>Plotly Dash Flask Tutorial</h1>
                                  </a>
                                <nav>
                                  <a href="/dashapp/"><i class="fas fa-chart-line"></i> Embdedded Plotly Dash</a>
                                </nav>
                            </div>
                            </header>
                            {%app_entry%}
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
