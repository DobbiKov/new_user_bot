from dataclasses import dataclass
from pyrogram import Client, filters
from pyrogram import types

from modules.database import create_chats_for_translating, select_chat_by_chatid
from data import database_connection
import datetime

async def my_trans_chats_handler(client: Client, message: types.Message):
    chats = await select_chat_by_chatid(database_connection, message.chat.id)
    if chats is None or chats is False:
        return await client.send_message(message.chat.id, f"You haven't any chats for translation!")

    keyboard = await generate_keyboard_by_chats(chats)
    await client.send_message(message.chat.id, f"List of the chats that I translate:", reply_markup=keyboard)


#(2, 'Querty Azerty', '2022-09-28 21:16:33.851907', 5200613842)
async def generate_keyboard_by_chats(chats):
    rows = [] #here is the rows of the chats

    row = [] #here is the chats inside the row
    iterator = 0
    for chat in chats:
        row.append(types.InlineKeyboardButton(  
                            chat[1],
                            callback_data=f"del_trans_chat_{chat[3]}"
                        )) #append the chat to the row
        iterator += 1
        print(f"{iterator}/{len(chats)}")
        if (iterator + 1) % 2 == 0: #if the iterator is deviding 2 that means that we have 2 chat in the row
            rows.append(row) #in this case we append row to the list of rows
            row = [] #and clear our list of chats in the row in order to put new chats
            continue
        if(iterator == len(chats)): #if iterator and length of the list of the chats are the same that mean that we haven't any chats and we have to append it to the rows
            rows.append(row) #in this case we append row to the list of rows
            row = [] #and clear our list of chats in the row in order to put new chats
    keyboard = types.InlineKeyboardMarkup(rows) 
    return keyboard
