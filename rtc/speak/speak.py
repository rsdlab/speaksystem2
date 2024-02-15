#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file speak.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

from gtts import gTTS
from playsound import playsound


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
speak_spec = ["implementation_id", "speak", 
         "type_name",         "speak", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class speak
# @brief ModuleDescription
# 
# 
# </rtc-template>
class speak(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_data_in = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._data_inIn = OpenRTM_aist.InPort("data_in", self._d_data_in)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("data_in",self._data_inIn)
		
        # Set OutPort buffers
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        print("speak:起動")
        text = "起動しました"
        # テキストを音声に変換
        tts = gTTS(text, lang='ja')  # 'ja'は（日本語）
        # 変換した音声を一時ファイルに保存（ファイル名: output.mp3）
        tts.save("output.mp3")
        # 保存した音声ファイルを再生
        playsound("output.mp3")
        # 一時ファイルを削除
        import os
        os.remove("output.mp3")
        '''
        text = "こんにちは"
        # テキストを音声に変換
        tts = gTTS(text, lang='ja')  # 'ja'は言語コードです（日本語）
        # 変換した音声を一時ファイルに保存（ファイル名: output.mp3）
        tts.save("output.mp3")
        # 保存した音声ファイルを再生
        playsound("output.mp3")
        # 一時ファイルを削除
        import os
        os.remove("output.mp3")
        '''
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        if self._data_inIn.isNew(): 
            self._d_data_in=self._data_inIn.read()
            print(self._d_data_in)

            if self._d_data_in.data==1:
                print("speak:おはよう")
                text = "おはよう"
                # テキストを音声に変換
                tts = gTTS(text, lang='ja')  # 'ja'は（日本語）
                # 変換した音声を一時ファイルに保存（ファイル名: output.mp3）
                tts.save("output.mp3")
                # 保存した音声ファイルを再生
                playsound("output.mp3")
                # 一時ファイルを削除
                import os
                os.remove("output.mp3")
            if self._d_data_in.data==2:
                print("speak:こんにちは")
                text = "こんにちは"
                # テキストを音声に変換
                tts = gTTS(text, lang='ja')  # 'ja'は（日本語）
                # 変換した音声を一時ファイルに保存（ファイル名: output.mp3）
                tts.save("output.mp3")
                # 保存した音声ファイルを再生
                playsound("output.mp3")
                # 一時ファイルを削除
                import os
                os.remove("output.mp3")
            
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def speakInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=speak_spec)
    manager.registerFactory(profile,
                            speak,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    speakInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("speak" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

