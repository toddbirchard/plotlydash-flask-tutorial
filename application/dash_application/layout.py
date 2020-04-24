html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body>
                            <header>
                              <div class="nav-wrapper">
                                <a href="/" class="logo">
                                    <img src="/static/img/logo.png" class="logo" />
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
