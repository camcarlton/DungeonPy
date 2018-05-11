# Generated from DungeonPy.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\2\3\3\3\3\6\3#\n\3\r\3\16\3$\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tA")
        buf.write("\n\t\3\n\3\n\3\n\3\13\3\13\3\13\6\13I\n\13\r\13\16\13")
        buf.write("J\3\13\3\13\3\13\3\13\5\13Q\n\13\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\3\3\2\7\b\2V\2\31\3\2\2\2\4")
        buf.write(" \3\2\2\2\6(\3\2\2\2\b,\3\2\2\2\n\60\3\2\2\2\f\63\3\2")
        buf.write("\2\2\16\65\3\2\2\2\20@\3\2\2\2\22B\3\2\2\2\24P\3\2\2\2")
        buf.write("\26R\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2")
        buf.write("\33\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\5\6\4")
        buf.write("\2\36\37\7\2\2\3\37\3\3\2\2\2 \"\5\b\5\2!#\5\n\6\2\"!")
        buf.write("\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\5")
        buf.write("\f\7\2\'\5\3\2\2\2()\7\t\2\2)*\5\26\f\2*+\7\13\2\2+\7")
        buf.write("\3\2\2\2,-\5\16\b\2-.\5\26\f\2./\5\20\t\2/\t\3\2\2\2\60")
        buf.write("\61\5\22\n\2\61\62\5\24\13\2\62\13\3\2\2\2\63\64\7\22")
        buf.write("\2\2\64\r\3\2\2\2\65\66\t\2\2\2\66\17\3\2\2\2\67A\7\13")
        buf.write("\2\28A\7\21\2\29A\7\n\2\2:A\7\20\2\2;A\7\f\2\2<A\7\r\2")
        buf.write("\2=A\7\16\2\2>A\7\17\2\2?A\3\2\2\2@\67\3\2\2\2@8\3\2\2")
        buf.write("\2@9\3\2\2\2@:\3\2\2\2@;\3\2\2\2@<\3\2\2\2@=\3\2\2\2@")
        buf.write(">\3\2\2\2@?\3\2\2\2A\21\3\2\2\2BC\7\3\2\2CD\5\26\f\2D")
        buf.write("\23\3\2\2\2EH\7\4\2\2FG\7\24\2\2GI\7\5\2\2HF\3\2\2\2I")
        buf.write("J\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\24\2\2MQ\7")
        buf.write("\6\2\2NQ\7\24\2\2OQ\7\23\2\2PE\3\2\2\2PN\3\2\2\2PO\3\2")
        buf.write("\2\2Q\25\3\2\2\2RS\7\25\2\2S\27\3\2\2\2\7\33$@JP")
        return buf.getvalue()


class DungeonPyParser ( Parser ):

    grammarFileName = "DungeonPy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BEGIN", "SET", "START", "LOCATION", 
                      "CAMPAIGN", "PLAYER", "LOOT", "CREATURE", "SHOP", 
                      "NPC", "REALM", "DONE", "INT", "STRING", "WORD", "WHITESPACE" ]

    RULE_game = 0
    RULE_setup = 1
    RULE_start = 2
    RULE_entity = 3
    RULE_action = 4
    RULE_done = 5
    RULE_command = 6
    RULE_cmd_type = 7
    RULE_key = 8
    RULE_value = 9
    RULE_idenity = 10

    ruleNames =  [ "game", "setup", "start", "entity", "action", "done", 
                   "command", "cmd_type", "key", "value", "idenity" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BEGIN=5
    SET=6
    START=7
    LOCATION=8
    CAMPAIGN=9
    PLAYER=10
    LOOT=11
    CREATURE=12
    SHOP=13
    NPC=14
    REALM=15
    DONE=16
    INT=17
    STRING=18
    WORD=19
    WHITESPACE=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(DungeonPyParser.StartContext,0)


        def EOF(self):
            return self.getToken(DungeonPyParser.EOF, 0)

        def setup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DungeonPyParser.SetupContext)
            else:
                return self.getTypedRuleContext(DungeonPyParser.SetupContext,i)


        def getRuleIndex(self):
            return DungeonPyParser.RULE_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame" ):
                listener.enterGame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame" ):
                listener.exitGame(self)




    def game(self):

        localctx = DungeonPyParser.GameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_game)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.setup()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DungeonPyParser.BEGIN or _la==DungeonPyParser.SET):
                    break

            self.state = 27
            self.start()
            self.state = 28
            self.match(DungeonPyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SetupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entity(self):
            return self.getTypedRuleContext(DungeonPyParser.EntityContext,0)


        def done(self):
            return self.getTypedRuleContext(DungeonPyParser.DoneContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DungeonPyParser.ActionContext)
            else:
                return self.getTypedRuleContext(DungeonPyParser.ActionContext,i)


        def getRuleIndex(self):
            return DungeonPyParser.RULE_setup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetup" ):
                listener.enterSetup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetup" ):
                listener.exitSetup(self)




    def setup(self):

        localctx = DungeonPyParser.SetupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_setup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.entity()
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.action()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==DungeonPyParser.T__0):
                    break

            self.state = 36
            self.done()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(DungeonPyParser.START, 0)

        def idenity(self):
            return self.getTypedRuleContext(DungeonPyParser.IdenityContext,0)


        def CAMPAIGN(self):
            return self.getToken(DungeonPyParser.CAMPAIGN, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = DungeonPyParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(DungeonPyParser.START)
            self.state = 39
            self.idenity()
            self.state = 40
            self.match(DungeonPyParser.CAMPAIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EntityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(DungeonPyParser.CommandContext,0)


        def idenity(self):
            return self.getTypedRuleContext(DungeonPyParser.IdenityContext,0)


        def cmd_type(self):
            return self.getTypedRuleContext(DungeonPyParser.Cmd_typeContext,0)


        def getRuleIndex(self):
            return DungeonPyParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = DungeonPyParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_entity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.command()
            self.state = 43
            self.idenity()
            self.state = 44
            self.cmd_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(DungeonPyParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(DungeonPyParser.ValueContext,0)


        def getRuleIndex(self):
            return DungeonPyParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = DungeonPyParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.key()
            self.state = 47
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DoneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DONE(self):
            return self.getToken(DungeonPyParser.DONE, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_done

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDone" ):
                listener.enterDone(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDone" ):
                listener.exitDone(self)




    def done(self):

        localctx = DungeonPyParser.DoneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_done)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DungeonPyParser.DONE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(DungeonPyParser.BEGIN, 0)

        def SET(self):
            return self.getToken(DungeonPyParser.SET, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = DungeonPyParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==DungeonPyParser.BEGIN or _la==DungeonPyParser.SET):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cmd_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAMPAIGN(self):
            return self.getToken(DungeonPyParser.CAMPAIGN, 0)

        def REALM(self):
            return self.getToken(DungeonPyParser.REALM, 0)

        def LOCATION(self):
            return self.getToken(DungeonPyParser.LOCATION, 0)

        def NPC(self):
            return self.getToken(DungeonPyParser.NPC, 0)

        def PLAYER(self):
            return self.getToken(DungeonPyParser.PLAYER, 0)

        def LOOT(self):
            return self.getToken(DungeonPyParser.LOOT, 0)

        def CREATURE(self):
            return self.getToken(DungeonPyParser.CREATURE, 0)

        def SHOP(self):
            return self.getToken(DungeonPyParser.SHOP, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_cmd_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd_type" ):
                listener.enterCmd_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd_type" ):
                listener.exitCmd_type(self)




    def cmd_type(self):

        localctx = DungeonPyParser.Cmd_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmd_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DungeonPyParser.CAMPAIGN]:
                self.state = 53
                self.match(DungeonPyParser.CAMPAIGN)
                pass
            elif token in [DungeonPyParser.REALM]:
                self.state = 54
                self.match(DungeonPyParser.REALM)
                pass
            elif token in [DungeonPyParser.LOCATION]:
                self.state = 55
                self.match(DungeonPyParser.LOCATION)
                pass
            elif token in [DungeonPyParser.NPC]:
                self.state = 56
                self.match(DungeonPyParser.NPC)
                pass
            elif token in [DungeonPyParser.PLAYER]:
                self.state = 57
                self.match(DungeonPyParser.PLAYER)
                pass
            elif token in [DungeonPyParser.LOOT]:
                self.state = 58
                self.match(DungeonPyParser.LOOT)
                pass
            elif token in [DungeonPyParser.CREATURE]:
                self.state = 59
                self.match(DungeonPyParser.CREATURE)
                pass
            elif token in [DungeonPyParser.SHOP]:
                self.state = 60
                self.match(DungeonPyParser.SHOP)
                pass
            elif token in [DungeonPyParser.T__0]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idenity(self):
            return self.getTypedRuleContext(DungeonPyParser.IdenityContext,0)


        def getRuleIndex(self):
            return DungeonPyParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = DungeonPyParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(DungeonPyParser.T__0)
            self.state = 65
            self.idenity()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(DungeonPyParser.STRING)
            else:
                return self.getToken(DungeonPyParser.STRING, i)

        def INT(self):
            return self.getToken(DungeonPyParser.INT, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = DungeonPyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DungeonPyParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(DungeonPyParser.T__1)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 68
                        self.match(DungeonPyParser.STRING)
                        self.state = 69
                        self.match(DungeonPyParser.T__2)

                    else:
                        raise NoViableAltException(self)
                    self.state = 72 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 74
                self.match(DungeonPyParser.STRING)
                self.state = 75
                self.match(DungeonPyParser.T__3)
                pass
            elif token in [DungeonPyParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(DungeonPyParser.STRING)
                pass
            elif token in [DungeonPyParser.INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(DungeonPyParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdenityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(DungeonPyParser.WORD, 0)

        def getRuleIndex(self):
            return DungeonPyParser.RULE_idenity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdenity" ):
                listener.enterIdenity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdenity" ):
                listener.exitIdenity(self)




    def idenity(self):

        localctx = DungeonPyParser.IdenityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idenity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(DungeonPyParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





