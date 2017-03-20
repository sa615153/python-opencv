#! /bin/bash

tr -sc "A-Za-z" "\n" < man.config|sort |uniq -c | sort -n -r |less

tr -'A-Z' 'a-z' <man.config |tr -sc 'A-Za-z' '\n' |sort |uniq -c | sort -n -r |less