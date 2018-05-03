# coding=utf-8
from __future__ import unicode_literals
import thread
import time
import nltk
import sys
from elections.api.config import TwitterAPI
from elections.utils.streamer import TweetsStreamer

''' Variables para minar datos por candidato'''
MEADE = ['Pepe Meade','Meade','Jose Antonio Meade','José Antonio Meade','Pepe Meade Yo Mero','Meade Yo Mero','Jose Antonio Meade Yo Mero','José Antonio Meade Yo Mero',
'Pepe Meade PRI','Meade PRI','Jose Antonio Meade PRI','José Antonio Meade PRI','Yo con Meade','Meade Partido Verde','Pepe Partido Verde','Pepe Meade Partido Verde',
'Jose Antonio Meade Partido Verde','José Antonio Meade Partido Verde','Pepe Meade PVEM', 'Meade PVEM','Jose Antonio Meade PVEM','José Antonio Meade PVEM',
'Pepe Meade Nueva Alianza', 'Meade Nueva Alianza','Jose Antonio Meade Nueva Alianza','José Antonio Meade Nueva Alianza','Pepe Meade Partido Nueva Alianza', 'Meade Partido Nueva Alianza',
'Jose Antonio Meade Partido Nueva Alianza','José Antonio Meade Partido Nueva Alianza','Pepe Meade PANAL', 'Meade PANAL','Jose Antonio Meade PANAL','José Antonio Meade PANAL',
'Pepe Meade Todos Por Mexico', 'Meade Todos Por Mexico','Jose Antonio Meade Todos Por Mexico','José Antonio Meade Todos Por Mexico',
'Pepe Meade Todos Por México', 'Meade Todos Por México','Jose Antonio Meade Todos Por México','José Antonio Meade Todos Por México',
'Pepe Meade Avanzar Contigo', 'Meade Avanzar Contigo','Jose Antonio Meade Avanzar Contigo','José Antonio Meade Avanzar Contigo']

AMLO = ['amlo','peje','andres manuel lopez obrador','andrés manuel lópez obrador','lopez obrador','lópez obrador',
'amlo juntos haremos historia','peje juntos haremos historia','pj juntos haremos historia','andres manuel lopez obrador juntos haremos historia',
'andrés manuel lópez obrador juntos haremos historia','lopez obrador juntos haremos historia','lópez obrador juntos haremos historia',
'andres manuel juntos haremos historia','andrés manuel juntos haremos historia',
'amlo morena','peje morena','pj morena','andres manuel lopez obrador morena','andrés manuel lópez obrador morena',
'lopez obrador morena','lópez obrador morena','andres manuel morena','andrés manuel morena', 
'amlo partido del trabajo','peje partido del trabajo','pj partido del trabajo','andres manuel lopez obrador partido del trabajo','andrés manuel lópez obrador partido del trabajo',
'lopez obrador partido del trabajo','lópez obrador partido del trabajo','andres manuel partido del trabajo','andrés manuel partido del trabajo',
'amlo pt','peje pt','pj pt','andres manuel lopez obrador pt','andrés manuel lópez obrador pt','lopez obrador pt','lópez obrador pt','andres manuel pt','andrés manuel pt',
'amlo encuentro social','peje encuentro social','pj encuentro social','andres manuel lopez obrador encuentro social','andrés manuel lópez obrador encuentro social',
'lopez obrador encuentro social','lópez obrador encuentro social','andres manuel encuentro social','andrés manuel encuentro social',
'amlo partido encuentro social','peje partido encuentro social','pj partido encuentro social','andres manuel lopez obrador partido encuentro social','andrés manuel lópez obrador partido encuentro social',
'lopez obrador partido encuentro social','lópez obrador partido encuentro social','andres manuel partido encuentro social','andrés manuel partido encuentro social']

ANAYA = ['Ricardo Anaya','Anaya','Ricardo Anaya Coalicion Por Mexico Al Frente','Anaya Coalicion Por Mexico Al Frente','Ricardo Anaya Coalicion Por México Al Frente','Anaya Coalicion Por México al Frente',
'Ricardo Anaya Movimiento Naranja','Anaya Movimiento Naranja','Ricardo Anaya Movimiento Ciudadano','Anaya Movimiento Ciudadano',
'Ricardo Anaya PAN','Anaya PAN','Ricardo Anaya PRD','Anaya PRD','Ricardo Anaya MC','Anaya MC','Ricardo Anaya Partido Accion Nacional','Anaya Partido Accion Nacional',
'Ricardo Anaya Partido Acción Nacional','Anaya Partido Acción Nacional','Ricardo Anaya Partdido Revolución Democrática','Anaya Partido Revolución Democrática',
'Ricardo Anaya De Frente al Futuro','Anaya De Frente al Futuro','Ricardo Anaya El México Que si Queremos','Anaya El México Que si Queremos','Ricardo Anaya El Mexico Que si Queremos','Anaya El Mexico Que si Queremos']

twitter_api = TwitterAPI()

def run_streamer(candidate_username):
    tweets_streamer = TweetsStreamer()
    tweets_streamer.set_candidate(candidate_username)
    myStream = twitter_api.tweepy.Stream(auth = twitter_api.api.auth, listener=tweets_streamer)

    if candidate_username == 'lopezobrador_':
        myStream.filter(track=AMLO)
    elif candidate_username == 'RicardoAnayaC':
        myStream.filter(track=ANAYA)
    elif candidate_username == 'JoseAMeadeK':
        myStream.filter(track=MEADE)

if __name__ == "__main__":
    run_streamer(sys.argv[1])