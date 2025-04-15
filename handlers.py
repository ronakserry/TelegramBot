from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler, MessageHandler, filters
from datetime import datetime
import sqlite3
import DbConnection as Db
Name, Price, Stock, Category, Description = range(5)
async def add_product(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        "اسم محصول:"
    )
    return Name

async def product_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text(
        'قیمت محصول:'
    )
    return Price

async def product_price(update: Update, context: CallbackContext) -> int:
    context.user_data['price'] = update.message.text
    await update.message.reply_text(
        'موجودی:'
    )
    return Stock

async def product_stock(update: Update, context: CallbackContext) -> int:
    context.user_data['stock'] = update.message.text
    await update.message.reply_text(
        'دسته بندی:'
    )
    return Category

async def product_category(update: Update, context: CallbackContext) -> int:
    context.user_data['category'] = update.message.text
    await update.message.reply_text(
        'توضیحات:'
    )
    return Description

async def product_description(update: Update, context: CallbackContext) -> int:
    context.user_data['description'] = update.message.text
    product_data = {
        'name': context.user_data['name'],
        'price': context.user_data['price'],
        'stock': context.user_data['stock'],
        'category': context.user_data['category'],
        'description': context.user_data['description'],
        'created_at': datetime.now()
    }
    await Db.insert_product(product_data)
    await update.message.reply_text(
        'Product added successfully!'
    )
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        'Product addition cancelled.'
    )
    return ConversationHandler.END

product_conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Text('Add Product'), add_product)],
    states={
        Name: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_name)],
        Price: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_price)],
        Stock: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_stock)],
        Category: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_category)],
        Description: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_description)],
    },
    fallbacks=[MessageHandler(filters.COMMAND, cancel)]
)

__all__ = ['product_conversation_handler']

async def insert_product(product_data):
    conn = sqlite3.connect("BotDb.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Products (ProName, ProStock, ProPrice, CategoryID, CreatedAt, UpdatedAt, Describtion)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product_data['name'],
        product_data['stock'],
        product_data['price'],
        product_data['category'],
        product_data['created_at'],
        product_data['created_at'],
        product_data['description']
    ))
    conn.commit()
    conn.close()

async def product_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text(
        'قیمت محصول:'
    )
    return Price

async def product_price(update: Update, context: CallbackContext) -> int:
    context.user_data['price'] = update.message.text
    await update.message.reply_text(
        'موجودی محصول:'
    )
    return Stock

async def product_stock(update: Update, context: CallbackContext) -> int:
    context.user_data['stock'] = update.message.text
    await update.message.reply_text(
        'دسته بندی:'
    )
    return Category

async def product_category(update: Update, context: CallbackContext) -> int:
    context.user_data['category'] = update.message.text
    await update.message.reply_text(
        'توضیحات:'
    )
    return Description

async def product_description(update: Update, context: CallbackContext) -> int:
    context.user_data['description'] = update.message.text
    product_data = {
        'name': context.user_data['name'],
        'price': context.user_data['price'],
        'stock': context.user_data['stock'],
        'category': context.user_data['category'],
        'description': context.user_data['description'],
        'created_at': datetime.now()
    }
    await insert_product(product_data)
    await update.message.reply_text(
        'محصول با موفقیت اضافه شد!'
    )
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        'اضافه کردن محصول لغو شد.'
    )
    return ConversationHandler.END

product_conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Text('AddProduct'), product_name)],
    states={
        Name: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_name)],
        Price: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_price)],
        Stock: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_stock)],
        Category: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_category)],
        Description: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_description)],
    },
    fallbacks=[MessageHandler(filters.COMMAND, cancel)]
)

__all__ = ['product_conversation_handler']

