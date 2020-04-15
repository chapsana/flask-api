# -*- encoding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

	
	SECRET_KEY   = "77tgFCdrEEdv77554##@3" 
	
	SQLALCHEMY_TRACK_MODIFICATIONS 	= False

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
