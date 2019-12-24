mailx -v -s "this is a test" \
-S smtp=smtp://127.0.0.1 \
-S from="ryan@example.com(Ryan Faircloth)" \
-S ssl-verify=ignore \
-S smtp-use-starttls \
archiver@stoq.spl.guru