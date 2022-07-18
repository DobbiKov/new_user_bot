def helpall(client, message):
    client.send_message(message.chat.id, "\
The list of commands:\n\n\
- #23 - google search\n\
- #fr - to translate from ukrainian to french quickly\n\
- #ua - to translate from french to ukrainian quickly\n\n\
- #en - to translate from russian to english\n\
- #ru - to translate from english to russian")