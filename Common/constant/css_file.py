#homesis
class CSS:
    class homesis_css:
        #CSS to style a upload file button in change role in bank section
        css = '''
        <style>
            div[data-testid="column"]:has(>div>div>div>div[data-testid="element-container"] >div[data-testid='stFileUploader']) {
                width: max-content;
            }
            div[data-testid="column"]:has(>div>div>div>div[data-testid="element-container"] >div[data-testid='stFileUploader']) section {
                padding: 0;
                float: left;
            }
            div[data-testid="column"]:has(>div>div>div>div[data-testid="element-container"] >div[data-testid='stFileUploader']) section > input + div {
                display: none;
            }
            div[data-testid="column"]:has(>div>div>div>div[data-testid="element-container"] >div[data-testid='stFileUploader']) section + div {
                float: right;
                padding-top: 0;
            }

        </style>
         '''