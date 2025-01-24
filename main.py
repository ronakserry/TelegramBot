from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from config import BotToken
import pyodbc 

# commands
async def StartCommand(update: Update, context: CallbackContext) -> None:
    buttons = [
        [InlineKeyboardButton("اکانت", callback_data='AccountCommand')],
        [InlineKeyboardButton("محصولات", callback_data='ProductsCommand')],
        [InlineKeyboardButton("آنالیز فروش", callback_data='AnalysCommand')],
        [InlineKeyboardButton("اطلاعات", callback_data='InfoCommand')],
        [InlineKeyboardButton("ساپورت", callback_data='HelpCommand')],
        [InlineKeyboardButton("تنظیمات", callback_data='SettingCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if update.callback_query:
        await update.callback_query.edit_message_text('یه بخش دیگه رو انتخاب کن لطفا', reply_markup=reply_markup)
    elif update.message:
        await update.message.reply_text('خوش اومدی، چه کمکی از دستم برمیاد؟', reply_markup=reply_markup)

async def ProductsCommand(update: Update, context: CallbackContext):
    ProBtn = [
        [InlineKeyboardButton("اضافه کردن محصول", callback_data="AddProduct")],
        [InlineKeyboardButton("مشاهده محصولات", callback_data='ViewProducts')],
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')] 
    ]
    reply_markup = InlineKeyboardMarkup(ProBtn)
    await update.callback_query.edit_message_text("محصولات", reply_markup=reply_markup)

async def AddProduct(update: Update, context: CallbackContext):
    AddBtn = [
        [InlineKeyboardButton("ادامه", callback_data='AddProduct')], 
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(AddBtn) 
    await update.callback_query.edit_message_text("از اینجا میتونی محصول جدید وارد کنی. ", reply_markup=reply_markup)  

async def ViewProducts(update: Update, context: CallbackContext):
    ViewBtn=[
        [InlineKeyboardButton("بازگشت",callback_data="StartCommand")]
    ]
    reply_markup = InlineKeyboardMarkup(ViewBtn)
    await update.callback_query.edit_message_text("از اینجا می‌تونی محصولاتت رو ببینی.", reply_markup=reply_markup)
async def AccountCommand(update: Update, context: CallbackContext):
    AccBtn = [
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(AccBtn)
    await update.callback_query.edit_message_text("این بخش در حال حاضر کار نمیکنه ولی در آینده میتونین ازش نوع اکانت و مدت زمان اکانت رو مشخص کنین، در حال حاضر فقط بخش فروشنده کار میکنه.", reply_markup=reply_markup)

async def AnalysCommand(update: Update, context: CallbackContext):
    AnalyseBtn = [
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(AnalyseBtn)
    await update.callback_query.edit_message_text("این بخش هم کار نمی‌کنه ولی درآینده می‌تونین ازش آمار فروش رو ببینین.", reply_markup=reply_markup)

async def InfoCommand(update: Update, context: CallbackContext):
    InfoBtn = [
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(InfoBtn)
    await update.callback_query.edit_message_text("این یه پروژه تمرینی هست و در حال حاضر قابلیت استفاده برای کانال‌های واقعی رو نداره.", reply_markup=reply_markup)

async def HelpCommand(update: Update, context: CallbackContext):
    HelpBtn = [
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(HelpBtn)
    await update.callback_query.edit_message_text("تو گیت هاب یا لینکداین با من در ارتباط باشین", reply_markup=reply_markup)

async def SettingCommand(update: Update, context: CallbackContext):
    SettBtn = [
        [InlineKeyboardButton("بازگشت", callback_data='StartCommand')]
    ]
    reply_markup = InlineKeyboardMarkup(SettBtn)
    await update.callback_query.edit_message_text("تنظیمات ", reply_markup=reply_markup)

# Callback query handler
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'AccountCommand':
        await AccountCommand(update, context)
    elif query.data == 'ProductsCommand':
        await ProductsCommand(update, context)
    elif query.data == 'AnalysCommand':
        await AnalysCommand(update, context)
    elif query.data == 'InfoCommand':
        await InfoCommand(update, context)
    elif query.data == 'HelpCommand':
        await HelpCommand(update, context)
    elif query.data == 'SettingCommand':
        await SettingCommand(update, context)
    elif query.data == 'StartCommand': 
        await StartCommand(update, context)
    elif query.data == 'AddProduct':
        await AddProduct(update, context)
    elif query.data == 'ViewProducts':
        await ViewProducts(update, context) 
    else:
        await context.bot.send_message(query.from_user.id, "متوجه نشدم، چه کار کنم؟")

# Error handling
async def Error(update: Update, context: CallbackContext):
    print(f'update: {update} caused error: {context.error}')

# Putting it together
if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(BotToken).read_timeout(30).write_timeout(30).build()
    app.add_handler(CommandHandler('start', StartCommand))
    app.add_handler(CallbackQueryHandler(button))
    app.add_error_handler(Error)
    print('polling...')
    app.run_polling(poll_interval=1)

