from telethon import TelegramClient, events, Button, types
import random

# --- إعدادات البوت ---
API_ID = 37620915
API_HASH = "b5ba3ea198e5ebc87989b0b3c78652fe"
BOT_TOKEN = "8231710623:AAEQJ82nMpudPV_Cy_53Rcc8nOl9KOy6hbM" 

client = TelegramClient('toji_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

DEVPY_GROUPS = [] 

# --- [ قائمة الصور - 10 روابط ] ---
TOJI_IMAGES = [
    "https://j.top4top.io/p_3655qwvwn0.jpg", "https://k.top4top.io/p_3655y4foq1.jpg",
    "https://l.top4top.io/p_365569y2j2.jpg", "https://a.top4top.io/p_3655tymou3.jpg",
    "https://b.top4top.io/p_36550xoi64.jpg", "https://c.top4top.io/p_3655fkurp5.jpg",
    "https://d.top4top.io/p_3655j53b76.jpg", "https://e.top4top.io/p_36553jffu7.jpg",
    "https://f.top4top.io/p_3655mtnec8.jpg", "https://g.top4top.io/p_3655fm9ri9.jpg"
]

# --- [ قائمة الفيديوهات - 10 روابط ] ---
TOJI_DESIGNS = [
    "https://b.top4top.io/m_3655p8rwt0.mp4", "https://c.top4top.io/m_36556ifk31.mp4",
    "https://d.top4top.io/m_3655fe4012.mp4", "https://e.top4top.io/m_3655wf3fu3.mp4",
    "https://f.top4top.io/m_3655dhsoh4.mp4", "https://g.top4top.io/p_3655pdc5y5.mp4",
    "https://h.top4top.io/m_3655krlcx6.mp4", "https://i.top4top.io/m_3655j1ubp7.mp4",
    "https://j.top4top.io/m_36556duws8.mp4", "https://k.top4top.io/m_365568ssy9.mp4"
]

# --- [ الأغاني ] ---
CHANNEL_USERNAME = "X_C_T_O_J_I"
ALGERIAN_IDS = [711, 717, 726, 729, 735, 738, 750, 762, 777, 780, 783, 789]
TUNISIAN_IDS = [798, 801, 804, 807, 813, 816, 819, 822, 825, 831, 834, 837, 858, 861, 864, 867, 870, 873, 876, 891, 894, 897, 900, 921, 927, 930, 933, 936, 939, 942]

# --- [ الكليشات ] ---
START_VIDEO = "https://f.top4top.io/m_3657tukq62.mp4"
TOJI_START_TEXT = """⚔️ **𝐓𝐎𝐉𝐈 𝐔𝐒ＥＲＢ𝐎𝐓** ⚔️
”لا توجد قيمة للأشياء التي لا يمكن حمايتها.. وأنا هنا لأكون الدرع والسيف.“

🥷 **مـعـلـومـات الـنـظـام :**
- الاسـم : تـوجـي | **𝐓𝐨𝐣𝐢**
- الـمـطـور : [ **𝑴𝒂𝒔𝒕𝒆𝒓** ]
- الإصـدار : **𝑽.1.0**
- الـحـالـة : فـي وضـع الاسـتـعـداد.. ⚡️

⛩️ **سـورس تـوجـي 2026** ⛩️"""

COMMANDS_TEXT = """™️**Xc_GOAT_+216**

**الاوامر**
- أهلاً بك عزيزي في قائمة الاوامر :
━━━━━━━━━━━━━━
▫️ م1 : اوامر الادمنيه
▫️ م2 : اوامر الاعدادات
▫️ م3 : اوامر القفل - الفتح
▫️ م4 : اوامر التسليه
▫️ م5 : اوامر Dev
▫️ م6 : الاوامر الخدميه
━━━━━━━━━━━━━━"""

BUY_TEXT = """💳 **طـلـب سـورس تـوجـي الـخـاص** 💳

عزيزي المستخدم، يمكنك الآن الحصول على نسختك الخاصة من **بـوت تـوجـي** بأعلى المواصفات وأقوى حماية للمجموعات.

✨ **مـمـيـزات الـسـورس :**
• سـرعـة خـارقة فـي الرد والـتـنـفـيذ. ⚡️
• حـماية مـتـكاملة مـن الـتخريب والـسـبام. 🛡️
• لـوحـة تـحـكـم سـهـلة لـلـمـطورين. ⚙️
• تـحـديـثات مـسـتـمرة ودعـم فـني. 🛠️

👤 **لـلـشـراء والاسـتـفسـار تـواصـل مـع الـمـطـور :**
📍 المعرف: @C_R_B_X
━━━━━━━━━━━━━━"""

# دالة المنشن والروابط
def get_mention(user):
    return f"[{user.first_name}](tg://user?id={user.id})" if user else "المشرف"

def get_chat_link(chat):
    clean_id = str(chat.id).replace("-100", "")
    return f"[{chat.title}](https://t.me/c/{clean_id}/1)"

# --- [ التفعيل التلقائي ] ---
@client.on(events.ChatAction)
async def auto_activate(event):
    if event.user_joined or event.added_by:
        me = await client.get_me()
        if event.user_id == me.id:
            chat = await event.get_chat()
            if chat.id not in DEVPY_GROUPS:
                DEVPY_GROUPS.append(chat.id)
                adder = await event.get_added_by()
                await event.respond(f"™️**Xc_GOAT_+216**\n\n• المجموعه : {get_chat_link(chat)}\n• مفعله بنجاح ✅\n• بواسطة : {get_mention(adder)}", link_preview=False)

# --- [ أوامر المجموعة ] ---
@client.on(events.NewMessage)
async def group_handler(event):
    if not event.is_group: return 
    msg, chat_id = event.raw_text, event.chat_id
    chat = await event.get_chat()

    if msg == "تفعيل":
        if chat_id in DEVPY_GROUPS:
            await event.reply(f"™️**Xc_GOAT_+216**\n\n• المجموعه : {get_chat_link(chat)}\n• مفعله سابقاً ✅", link_preview=False)
        else:
            DEVPY_GROUPS.append(chat_id)
            user = await event.get_sender()
            await event.reply(f"™️**Xc_GOAT_+216**\n\n• المجموعه : {get_chat_link(chat)}\n• مفعله بنجاح ✅\n• بواسطة : {get_mention(user)}", link_preview=False)

    elif msg == "الاوامر" and chat_id in DEVPY_GROUPS:
        btns = [
            [Button.inline("❶", b"m1"), Button.inline("❷", b"m2"), Button.inline("❸", b"m3")],
            [Button.inline("اوامر Dev", b"m5"), Button.inline("اوامر التسليه", b"m4")],
            [Button.inline("اوامر خدميه", b"m6")],
            [Button.inline("القفل والفتح", b"m3"), Button.inline("التفعيل والتعطيل", b"m2")]
        ]
        await event.reply(COMMANDS_TEXT, buttons=btns)

# --- [ الخاص والأزرار ] ---
@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    if not event.is_private: return 
    reply_kb = [[Button.text("( صور توجي 📸 )", resize=True), Button.text("( تصاميم توجي 🎬 )", resize=True)],
                [Button.text("( أغاني جزائرية 🇩🇿 )", resize=True), Button.text("( أغاني تونسية 🇹🇳 )", resize=True)],
                [Button.text("( شراء بوت 💳 )", resize=True)]]
    
    await client.send_file(event.chat_id, START_VIDEO, caption=TOJI_START_TEXT, buttons=[[Button.url("مـطـور تـوجـي 👤", "https://t.me/C_R_B_X")], [Button.url("أضـف تـوجـي لـمـجـموعـتـك ➕", "https://t.me/C_R_B_X255BOT?startgroup=true")]])
    await event.respond("🛡️ تم تفعيل واجهة توجي بنجاح ✅", buttons=reply_kb)

@client.on(events.NewMessage)
async def buttons_reply(event):
    msg, chat = event.raw_text, event.chat_id
    if "( صور توجي 📸 )" in msg: await client.send_file(chat, random.choice(TOJI_IMAGES))
    elif "( تصاميم توجي 🎬 )" in msg: await client.send_file(chat, random.choice(TOJI_DESIGNS))
    elif "( أغاني جزائرية 🇩🇿 )" in msg: await client.send_message(chat, "🇩🇿 **𝐓𝐎𝐉𝐈 𝐀𝐋𝐆𝐄𝐑𝐈𝐀**", file=f"https://t.me/{CHANNEL_USERNAME}/{random.choice(ALGERIAN_IDS)}")
    elif "( أغاني تونسية 🇹🇳 )" in msg: await client.send_message(chat, "🇹🇳 **𝐓𝐎𝐉𝐈 𝐓𝐔𝐍𝐈𝐒𝐈𝐀**", file=f"https://t.me/{CHANNEL_USERNAME}/{random.choice(TUNISIAN_IDS)}")
    elif "( شراء بوت 💳 )" in msg: 
        await event.reply(BUY_TEXT, buttons=[Button.url("تـواصـل مـع الـمـطـور الآن 📥", "https://t.me/C_R_B_X")])

@client.on(events.CallbackQuery)
async def callback(event):
    map_data = {b"m1": "اوامر الادمنيه", b"m2": "اوامر الاعدادات", b"m3": "اوامر القفل", b"m4": "اوامر التسليه", b"m5": "اوامر المطور", b"m6": "الاوامر الخدميه"}
    if event.data in map_data:
        await event.edit(f"™️**Xc_GOAT_+216**\n\n{map_data[event.data]}")

print("✅ TOJI BOT IS LIVE & READY!")
client.run_until_disconnected()
              
