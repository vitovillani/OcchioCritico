import os

import feedparser

import openai

from flask import Flask

from threading import Thread

from telegram import Update

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes




