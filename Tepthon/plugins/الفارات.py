# Tepthon
# Copyright (C) 2022 TepthonArabic. All Rights Reserved
#
# This file is a part of < https://github.com/TepthonArabic/TepthonAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TepthonArabic/TepthonAr/blob/master/LICENSE/>.

""" وصـف الملـف : أوامـر اضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
اضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@E_7_V - كتـابـة الملـف: روجــر"""
# بــاقــر يولـد هههههههههههههههههههههههههه
import asyncio
import math
import os

import heroku3
import requests
import urllib3
import random
import string
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_display_name
from urlextract import URLExtract

from Tepthon import zedub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import delete_conv
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
from . import BOTLOG_CHATID, mention


plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

extractor = URLExtract()
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


Baqir_vars_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - أوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائمـة اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ أول مـرة ع سـورس تيبثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الاوامر` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة السورس` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف فار صورة البوت` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة أوامـر الفـارات\n\n\n"
    "**⎉╎قائمـة اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف خط الايدي` بالـرد ع الخـط او المستقيـم\n\n\n"
    "**⎉╎قائمـة اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف كليشة الحماية` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة الفحص` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة الحظر` بالـرد ع الكليشـة\n\n"
    "⪼ `.اضف كليشة البوت` بالـرد ع الكليشـة لـ اضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف كروب الرسائل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف كروب السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب` + اسـم الفـار\n\n"
    "⪼ `.حذف` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالأوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝙑𝙖𝙧𝙨 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 TepthonArabic . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    zed = await edit_or_reply(event, "**⎉╎جـاري اضـافة الفـار الـى بـوتك ...**")
    # All Rights Reserved for "Tepthon" "محمـد"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "كليشة الحظر" or input_str == "كليشه الحظر":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الآن قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMZED"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMZED") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك خاص`".format(input_str, vinfo))
        delgvar("Custom_Pm_Channel")
        addgvar("Custom_Pm_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للخـاص\
                        \n**- القنـاة {input_str} تم اضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "اشتراك كروب" or input_str == "اشتراك الكروب":
        variable = "Custom_G_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_G_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الآن** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم اضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Rep"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Rep") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "R_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("R_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الآن قـم بـ ارسـال الامـر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` إذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق إذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف إليه :**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "رسائل الحماية" or input_str == "رسائل الحمايه" or input_str == "رسائل الخاص" or input_str == "رسائل حماية الخاص" or input_str == "عدد التحذيرات":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "✾╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` إذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق إذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "MAX_FLOOD_IN_PMS"
        await asyncio.sleep(1.5)
        if vinfo.isdigit():
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        else:
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع رقـم فقـط ؟!**")
        heroku_var[variable] = vinfo

    elif input_str == "كود تيرمكس" or input_str == "كود السيشن" or input_str == "كود سيشن":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` إذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق إذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "STRING_SESSION"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف إليه :**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo

    elif input_str == "كروب الرسائل" or input_str == "كروب التخزين" or input_str == "كروب الخاص":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` إذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق إذا كنت لاتعلم.")
        heroku_var = app.config()
        variable = "PM_LOGGER_GROUP_ID"
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️** \n**⎉╎المضاف إليه :**\n `{}` \n**⎉╎يتم الآن اعـادة تشغيـل بـوت تيبثـــون يستغـرق الأمر 2-1 دقيقـة ▬▭ ...**".format(input_str, vinfo))
        heroku_var[variable] = vinfo
    elif input_str == "السجل" or input_str == "كروب السجل":
        if Config.HEROKU_API_KEY is None:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` إذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")

        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            return await ed(event, "⎉╎اضبط Var المطلوب في Heroku على وظيفة هذا 
