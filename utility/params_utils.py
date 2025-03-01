import yaml
import argparse
import os
from io import StringIO
import numpy as np
import pandas as pd
import pandas.io.sql as pndsql

class ParamsUtils:
    #returns a keyvaluepair list of the section name passed in the method
	#from the params.yaml file
    @classmethod
    def get_configuration(self, file_name = '', section = '',  sub_section = ''):
        __args = argparse.ArgumentParser()
        __path = os.getcwd() +"/Configuration/" + file_name
        __args.add_argument('--config', default = __path)
        __parsed_args = __args.parse_args()

        with open(__parsed_args.config) as yaml_file:
            config=yaml.safe_load(yaml_file)

        if(section == ''):
            return config
        elif(sub_section == ''):
            return config[section]
        else:
            return config[section][sub_section]			
				
    # # @classmethod
    # # def getAllConfiguration(self, adataframe):
    # #     #Declare dictionary object for tenant config and tenant data query
    # #     dicAllConfig = configDictionary()
	# # 	#Iterate key, value pair in a configuration file
    # #     for index, row in adataframe.iterrows():
    # #         if row["isenabled"] == 1:
    # #             dicConfig = configDictionary()
    # #             atConfig = ParamsUtils.get_configuration(row["tenantconfigfile"])
    # #             atQuery = ParamsUtils.get_configuration(row["dataqueryfile"])
    # #             dicConfig.add(0, row["source_schema"])
    # #             dicConfig.add(1, row["prediction_schema"])
    # #             dicConfig.add(2, atConfig)
    # #             dicConfig.add(3, atQuery)
    # #             dicAllConfig.add(int(row["tenantid"]), dicConfig)
	# # 		#End if tenant isenabled
	# # 	#end of for loop
    # #     return dicAllConfig
				
    # # @classmethod
    # # def get_selected_tenantconfig(self, aConfiguration, aTagKey = None, aTagValue = None):
	# # 	#Iterate key, value pair in a configuration file to find a particular tag file
    # #     for k, v in aConfiguration.items():
    # #         print(str(aConfiguration[k][str(aTagKey)]))
    # #         print(str(aTagValue))
    # #         if str(aConfiguration[k][aTagKey]) == str(aTagValue):
    # #             return aConfiguration[k]
	# # 		#end if search tag
	# # 	#end for loop

	# # 	#Return none if no tag value found
    # #     return None

				
    # @classmethod
    # def add_columns_to_distinguish_different_conf(self, df,input_value_type,type_of_distance,\
    #     power_on_off_status,module_option = 0):
    #     if df is not None:
    #         df["input_value_type"] = input_value_type
    #         df["type_of_distance"] = type_of_distance
    #         df["power_on_off_status"] = power_on_off_status
    #         df["moduleoption"] = module_option 
    #     #End of if

    #     return df
    
    # @classmethod
    # def get_sip_no_from_time(self, time, sip_duration_in_minutes):
    #     sip = int(time) / (60 * sip_duration_in_minutes)
    #     return sip



