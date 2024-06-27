# Zed-Thon
# Copyright (C) 2022 Zed-Thon . All Rights Reserved
#
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

""" وصـف الملـف : اوامـر اضـافة الفـارات باللغـة العربيـة كـاملة ولا حـرف انكلـش🤘 تخمـط اذكـر المصـدر يولـد
اضـافة فـارات صـورة ( الحمايـة - الفحـص - الوقتـي ) بـ امـر واحـد فقـط
حقـوق للتـاريخ : @Tepthon
@zzzzl1l - كتـابـة الملـف :  زلــزال الهيبــه"""
#زلـزال_الهيبـه يولـد هههههههههههههههههههههههههه
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
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from telethon.utils import get_display_name
from urlextract import URLExtract

from . import zedub

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


ZelzalVP_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 𝗩𝗮𝗿𝘀 - اوامـر الفـارات](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :** \n\n"
    "⪼ `.اضف صورة الحماية` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة الفحص` بالـرد ع صـورة او ميديـا\n"
    "⪼ قنـاة كلايـش الفحـص @tepthonkalesh\n\n"
    "⪼ `.اضف صورة الوقتي` بالـرد ع صـورة او ميديـا\n\n"
    "⪼ `.اضف صورة البوت` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة ستـارت للبـوت\n\n"
    "⪼ `.اضف صورة الحظر` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة لـ كليشـة الحظـر\n\n"
    "⪼ `.اضف صورة الكتم` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة لـ كليشـة الكتـم\n\n"
    "⪼ `.اضف صورة البلوك` بالـرد ع صـورة او ميديـا لـ اضـافة صـورة لـ كليشـة حظـر الخـاص\n\n"
    "⪼ `.اوامر الفارات` لعـرض بقيـة اوامـر الفـارات\n\n\n"
    "**⎉╎قائـمه اوامر تغييـر كليشـة الايـدي :** \n\n"
    "⪼ `.اضف فار ايموجي الايدي` بالـرد ع الرمـز او الايموجـي\n\n"
    "⪼ `.اضف فار عنوان الايدي` بالـرد ع نـص العنـوان\n\n"
    "⪼ `.اضف فار خط الايدي` بالـرد ع الخـط او المستقيـم\n\n"
    "⪼ `.اضف كليشة الايدي` بالـرد ع الكليشـه مـن القنـاة @tepthonkalesh \n\n\n"
    "**⎉╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :** \n\n"
    "⪼ `.اضف فار كليشة الحماية` بالـرد ع الكليشـة\n"
    "⪼ `.اضف فار كليشة البلوك` بالـرد ع الكليشـة لتغييـر كليشة الحظر خاص\n"
    "⪼ قنـاة كلايـش حمايـة الخـاص @tepthonkalesh\n\n"
    "⪼ `.اضف فار كليشة الفحص` بالـرد ع الكليشـة\n"
    "⪼ قنـاة كلايـش الفحـص @tepthonkalesh\n\n"
    "⪼ `.اضف فار كليشة البوت` بالـرد ع الكليشـة لـ اضـافة كليشـة ستـارت\n\n"
    "⪼ `.اضف فار زر الستارت` بالـرد ع يوزرك او يوزر قناتك لـ اضـافة زر الستـارت\n\n"
    "⪼ `.اضف فار رمز الوقتي` بالـرد ع رمـز\n\n"
    "⪼ `.اضف فار زخرفة الوقتي` بالـرد ع ارقـام الزغـرفه\n\n"
    "⪼ `.اضف فار البايو الوقتي` بالـرد ع البـايـو\n\n"
    "⪼ `.اضف فار اسم المستخدم` بالـرد ع اسـم\n\n"
    "⪼ `.اضف فار مجموعة التخزين` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار مجموعة السجل` بالـرد ع ايدي الكـروب\n\n"
    "⪼ `.اضف فار ايديي` بالـرد ع ايدي حسـابك\n\n"
    "⪼ `.اضف فار نقطة الاوامر` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نقطة المطور` بالـرد ع الـرمز الجديـد\n\n"
    "⪼ `.اضف فار نوم الترحيب` بالـرد ع رقـم الساعة لبداية نوم الترحيب المؤقت\n\n"
    "⪼ `.اضف فار ثواني لانهائي` بالـرد ع رقـم لعـدد الثوانـي الفاصـله بيـن كل عمليـة تجميـع فـي الأمــر لانهائـي\n\n"
    "⪼ `.اضف فار رسائل الحماية` بالـرد ع رقـم لعدد رسائل تحذيـرات حماية الخاص\n\n\n"
    "⪼ `.جلب فار` + اسـم الفـار\n\n"
    "⪼ `.حذف فار` + اسـم الفـار\n\n"
    "⪼ `.رفع مطور` بالـرد ع الشخـص لرفعـه مطـور تحكـم كامـل بالاوامـر\n\n"
    "⪼ `.حذف فار المطورين`\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "🛃 سيتـم اضـافة المزيـد من الدول قريبـاً\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


ZelzalTZ_cmd = (
    "𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الوقت](t.me/Tepthon) 𓆪\n\n"
    "**⎉╎قائـمه اوامر تغييـر المنطقـة الزمنيـة للوقـت 🌐:** \n\n"
    "⪼ `.وقت اليمن` \n\n"
    "⪼ `.وقت العراق` \n\n"
    "⪼ `.وقت السعودية` \n\n"
    "⪼ `.وقت سوريا` \n\n"
    "⪼ `.وقت مصر` \n\n"
    "⪼ `.وقت السودان` \n\n"
    "⪼ `.وقت ليبيا` \n\n"
    "⪼ `.وقت الامارات` \n\n"
    "⪼ `.وقت ايران` \n\n"
    "⪼ `.وقت الجزائر` \n\n"
    "⪼ `.وقت المغرب` \n\n"
    "⪼ `.وقت تركيا` \n\n"
    "⪼ `.وقت ماليزيا` \n\n"
    "⪼ `.وقت روسيا` \n\n"
    "⪼ `.وقت ايطاليا` \n\n"
    "⪼ `.وقت امريكا` \n\n"
    "🛃 سيتـم اضـافة المزيـد من الدول قريبـاً\n\n"
    "\n𓆩 [𝗧𝗲𝗽𝘁𝗵𝗼𝗻 𝗩𝗮𝗿𝘀 - قنـاة الفـارات](t.me/Tepthone1) 𓆪"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@zedub.zed_cmd(pattern=r"اضف فار (.*)")
async def variable(event):
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vinfo = reply.text
    zed = await edit_or_reply(event, "**⎉╎جـاري اضـافة الفـار الـى بـوتك ...**")
    # All Rights Reserved for "Zed-Thon" "زلـزال الهيبـه"
    if input_str == "كليشة الفحص" or input_str == "كليشه الفحص":
        variable = "ALIVE_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.فحص` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ALIVE_TEMPLATE", vinfo)
    elif input_str == "كليشة الحماية" or input_str == "كليشه الحمايه" or input_str == "كليشه الحماية" or input_str == "كليشة الحمايه":
        variable = "pmpermit_txt"
        await asyncio.sleep(1.5)
        if gvarstatus("pmpermit_txt") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.الحمايه تفعيل` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmpermit_txt", vinfo)
    elif input_str == "كليشة الايدي" or input_str == "كليشه الايدي":
        variable = "ZID_TEMPLATE"
        await asyncio.sleep(1.5)
        if gvarstatus("ZID_TEMPLATE") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.ايدي` **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("ZID_TEMPLATE", vinfo)
    elif input_str == "كليشة البوت" or input_str == "كليشه البوت" or input_str == "ستارت البوت" or input_str == "كليشة الستارت" or input_str == "كليشه الستارت" or input_str == "كليشة البدء":
        variable = "START_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الكليشـة المضـافه** \n {} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_TEXT", vinfo)
    elif input_str == "زر البوت" or input_str == "زر الستارت" or input_str == "زر ستارت":
        variable = "START_BUTUN"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("@"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع يـوزر فقـط**")
        vinfo = vinfo.replace("@", "")
        if gvarstatus("START_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم إضـافـة {} بنجـاح ☑️**\n**⎉╎رابـط زر كليشـة الستـارت الجـديـد** \nhttps://t.me/{} \n\n**⎉╎الان قـم بـ الذهـاب لبوتك المسـاعد من حساب آخر ↶** ودز ستارت **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("START_BUTUN", vinfo)
    elif input_str == "كليشة التوديع" or input_str == "كليشه التوديع" or input_str == "كليشة البلوك" or input_str == "كليشه البلوك":
        variable = "pmblock"
        await asyncio.sleep(1.5)
        if gvarstatus("pmblock") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ تفعيـل حماية الخاص عبر الامر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الكليشـة الجـديده** \n {} \n\n**⎉╎الان قـم بـ تفعيـل حماية الخاص عبر الامر ↶** ( `الحماية تفعيل` ) **لـ التحقـق مـن الكليشـة . .**".format(input_str, vinfo))
        addgvar("pmblock", vinfo)
    elif input_str == "رمز الوقتي" or input_str == "رمز الاسم الوقتي":
        variable = "CUSTOM_ALIVE_EMZED"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMZED") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الـرمـز الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافـة {} بنجـاح ☑️**\n**⎉╎الـرمـز المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.الاسم تلقائي` **لـ التحقـق مـن الـرمز . .**".format(input_str, vinfo))
    elif input_str == "البايو" or input_str == "البايو الوقتي" or input_str == "النبذه" or input_str == "البايو تلقائي":
        variable = "DEFAULT_BIO"
        await asyncio.sleep(1.5)
        if gvarstatus("DEFAULT_BIO") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـايـو الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافه {} بنجـاح ☑️**\n**⎉╎البـايـو المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.البايو تلقائي` **لـ التحقـق مـن البايـو . .**".format(input_str, vinfo))
    elif input_str == "التحقق" or input_str == "كود التحقق" or input_str == "التحقق بخطوتين" or input_str == "تحقق":
        variable = "TG_2STEP_VERIFICATION_CODE"
        await asyncio.sleep(1.5)
        if gvarstatus("TG_2STEP_VERIFICATION_CODE") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة {} بنجـاح ☑️**\n**⎉╎كـود التحـقق بخطـوتيـن** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.تحويل ملكية` **ثم معـرف الشخـص داخـل الكـروب او القنـاة . .**".format(input_str, vinfo))
    elif input_str == "كاشف الاباحي" or input_str == "كشف الاباحي":
        variable = "DEEP_API"
        await asyncio.sleep(1.5)
        if gvarstatus("DEEP_API") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن الجـديـد** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم إضافـة توكـن {} بنجـاح ☑️**\n**⎉╎التوكـن المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.قفل الاباحي` **لـ تفعيـل كاشـف الاباحي . .**".format(input_str, vinfo))
    elif input_str == "ايموجي الايدي" or input_str == "ايموجي ايدي" or input_str == "رمز الايدي" or input_str == "رمز ايدي" or input_str == "الرمز ايدي":
        variable = "CUSTOM_ALIVE_EMOJI"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_EMOJI") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_EMOJI", vinfo)
    elif input_str == "عنوان الايدي" or input_str == "عنوان ايدي":
        variable = "CUSTOM_ALIVE_TEXT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_TEXT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_TEXT", vinfo)
    elif input_str == "خط الايدي" or input_str == "خط ايدي" or input_str == "خطوط الايدي" or input_str == "خط ايدي":
        variable = "CUSTOM_ALIVE_FONT"
        await asyncio.sleep(1.5)
        if gvarstatus("CUSTOM_ALIVE_FONT") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.ايدي`".format(input_str, vinfo))
        addgvar("CUSTOM_ALIVE_FONT", vinfo)
    elif input_str == "اشتراك الخاص" or input_str == "اشتراك خاص":
        variable = "Custom_Pm_Channel"
        await asyncio.sleep(1.5)
        if gvarstatus("Custom_Pm_Channel") is None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك خاص`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك خاص`".format(input_str, vinfo))
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
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك كروب`".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n\n**⎉╎المتغيـر : ↶**\n `{}`\n**⎉╎ارسـل الان** `.اشتراك كروب`".format(input_str, vinfo))
        delgvar("Custom_G_Channel")
        addgvar("Custom_G_Channel", vinfo)
        if BOTLOG_CHATID:
                await event.client.send_message(
                BOTLOG_CHATID,
                f"#قنـاة_الاشتـراك_الاجبـاري_للكـروب\
                        \n**- القنـاة {input_str} تم اضافتهـا في قاعده البيانات ..بنجـاح ✓**",
            )
    elif input_str == "زاجل" or input_str == "قائمة زاجل" or input_str == "قائمه زاجل" or input_str == "يوزرات":
        variable = "ZAGL_Zed"
        await asyncio.sleep(1.5)
        if gvarstatus("ZAGL_Zed") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضافـة {} بنجـاح ☑️**\n**⎉╎اليـوزرات المضـافة** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.زاجل` **بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "سوبر" or input_str == "قائمة السوبر" or input_str == "قائمه السوبر" or input_str == "السوبرات" or input_str == "السوبر":
        variable = "Super_Id"
        await asyncio.sleep(1.5)
        if not vinfo.startswith("-100"):
            return await zed.edit("**⎉╎خطـأ .. قم بالـرد ع ارقـام ايديات المجموعات التي تبدأ ب 100- فقـط ؟!**\n**⎉╎قم بالذهاب لمجموعات السوبر التي تريد النشر فيها وكتابة الامر (.الايدي) ثم خذ ايدي المجموعة وهكذا لبقية المجموعات**")
        if gvarstatus("Super_Id") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضافـة {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎الايديات المضـافة** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** (`.سوبر` + عدد الثواني + عدد مرات التكرار)**بالـرد ع نـص او ميديـا بنـص . .**".format(input_str, vinfo))
    elif input_str == "بوت التجميع" or input_str == "بوت النقاط" or input_str == "النجميع" or input_str == "النقاط":
        variable = "Z_Point"
        await asyncio.sleep(1.5)
        if gvarstatus("Z_Point") is None:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
        else:
            addgvar(variable, vinfo)
            await zed.edit("**⎉╎تم اضـافه {} بنجـاح ☑️**\n**⎉╎البـوت المضـاف** \n {} \n\n**⎉╎الان قـم بـ ارسـال الأمــر ↶** `.تجميع` **لـ البـدء بتجميـع النقـاط من البـوت الجـديـد . .**".format(input_str, vinfo))
    elif input_str == "اسم المستخدم" or input_str == "الاسم":
        variable = "ALIVE_NAME"
        await asyncio.sleep(1.5)
        if gvarstatus("ALIVE_NAME") is not None:
            await zed.edit("**⎉╎تم تغييـر {} بنجـاح ☑️**\n**⎉╎المتغيـر : ↶**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت تيبثـــون يستغـرق الامر 2-1 دقيقــة ▬▭ ...**".format(input_str, vinfo))
        else:
            await zed.edit("**⎉╎تم اضافـة {} بنجـاح ☑️** \n**⎉╎المضاف إليــهِ :**\n `{}` \n**⎉╎يتم الان اعـادة تشغيـل بـوت تيبثـــون يستغـرق الامر 2-1 دقيقــة ▬▭ ...**".format(input_str, vinfo))
        addgvar(variable, vinfo)
    elif input_str == "رسائل 
