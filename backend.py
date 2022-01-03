# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restx import Resource, Api

app=Flask(__name__)
api=Api(app)

@api.route('/mypage')
class Me(Resource):
    def get(self):
        return {
            "name" : "조 한희",
            "hobby" : "차 마시기, 리코더 불기",
            "MBTI" : "ISTP",
            "email" : "hanhee.sw@gmail.com",
            "Github" : "github.com/seawavve",
            "LinkedIn" : "linkedin.com/in/seawavve"
                }

if __name__=='__main__':
    from waitress import serve
    serve(app, host='0.0.0.0',port=8081)