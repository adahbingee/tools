:: Generate a TOC for Markdown
:: https://www.ask-sheldon.com/create/
:: npm install -g doctoc

:: ### Markdown
:: Some text stuff gedöhns
:: ...
::  
:: <!-- START doctoc -->
:: <!-- END doctoc -->
::  
:: ...
:: Other Markdown stuff ...

::$> doctoc README.md --bitbucket # for Bitbucket format
::$> doctoc README.md --github    # for github.com format
::$> doctoc README.md --gitlab    # for gitlab.com format

:: doctoc %1 --gitlab
doctoc README.md --gitlab 