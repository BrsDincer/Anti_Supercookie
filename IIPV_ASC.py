import requests,json,random
from stem.control import Controller
from flask import Flask
from bs4 import BeautifulSoup
from optparse import OptionParser as OPTp



class COLOR_PICKING():
    END_COLOR = "\x1b[0m"
    GREEN_COLOR = "\033[1;32m"
    RED_COLOR = "\033[1;31m"
    YELLOW_COLOR = "\033[1;33m"
    INFO_COLOR = "\033[1;36m"
    
class PRINT_OPS():
    def GREEN_ECHO(echo_str=str):
        return COLOR_PICKING.GREEN_COLOR+echo_str+COLOR_PICKING.END_COLOR
    def RED_ECHO(echo_str=str):
        return COLOR_PICKING.RED_COLOR+echo_str+COLOR_PICKING.END_COLOR
    def YELLOW_ECHO(echo_str=str):
        return COLOR_PICKING.YELLOW_COLOR+echo_str+COLOR_PICKING.END_COLOR
    
class USER_OPS():
    def SHOW_INFO():
        try:
            print("""
                  
                  
             IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
             I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
             I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
             II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
               I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
               I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
               I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
               I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
               I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
               I::::I    I::::I            P::::P                       V:::::V V:::::V      
               I::::I    I::::I            P::::P                        V:::::V:::::V       
               I::::I    I::::I            P::::P                         V:::::::::V        
             II::::::IIII::::::II        PP::::::PP                        V:::::::V         
             I::::::::II::::::::I ...... P::::::::P                         V:::::V          
             I01000110II00110100I .::::. P01000110P                          V:::V     --> CREATED FOR FREE NET
             IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      --> open-source culture
                                                                                       --> ANTI-SUPERCOOKIE
                  
                 ############################################################################################################
                 ############################################################################################################
                 -------------------------------------------------------------------------------------
                 
                 py IIPV_ASC.py     -<TYPE> https://example.com      [or] py IIPV_ASC.py     --<TYPE>  https://example.com 
                 python IIPV_ASC.py -<TYPE> https://example.com      [or] python IIPV_ASC.py --<TYPE>  https://example.com
                 -------------------------------------------------------------------------------------
                 ############################################################################################################
                 ############################################################################################################
                  
                  -------------------------------------------------------------------------------------
                  ####   -h    --help             how to use   ####
                  
                  [ -r ]  --run                -> RUN PROCESS
                  [ -p ]  --proxyrun           -> RUN PROCESS WITH PROXIES
                  
                  -------------------------------------------------------------------------------------
                  
                  
                  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                  -------------------------------------------------------------------------------------
                  [NOTED - IMPORTANT]
                  + CHECK YOUR AUTHORIZATION SETTINGS FOR PROXY SEARCH
                  + USING VPN PROVIDES PREVENTION
                  + THE SITE MAY ALSO BE PROHIBITED IN THE COUNTRY OF THE PROX YOU FIND
                  + JUST REFRESH THE TOR PAGE FOR A NEW PROXY
                  + YOU DO NOT HAVE TO USE A PROXY IF THE SITE YOU ARE SEARCHING IS NOT BANNED IN YOUR COUNTRY
                  -------------------------------------------------------------------------------------
                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                  
                  
                  """)
        except:
            pass
    
    def USER_AGENT_LIST():
        try:
            global list_agent
            Json_Tar="user_agent_all.json"
            f_op = open(Json_Tar)
            j_op = json.loads(f_op.read())
            list_agent = []
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_agent.append(ixlp_values)
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))

    
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",errors="replace") as file_tar:
                x_file = []
                for line_x in file_tar:
                    try:
                        ext_tar = line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
            pass
        
    def PROXY_LIST():
        try:
            Rand_Url_Main = "https://free-proxy-list.net/"
            USER_OPS.USER_AGENT_LIST()
            user_agent_all = {"User-Agent":f"{random.choice(list_agent)}"}
            Soup_Main = BeautifulSoup(requests.get(Rand_Url_Main,headers=user_agent_all).content, "html.parser")
            IP_List = []
            PR_List = []
            i_count_spoof = 0
            for tab_all in Soup_Main.find("table",class_="table table-striped table-bordered"):
                tr_all = tab_all.find_all("tr")
                for x_tr in tr_all:
                    td_all = x_tr.find_all("td")
                    for x_td in td_all:
                        i_count_spoof += 1
                        if i_count_spoof == 1:
                            IP_M = x_td.text
                            IP_List.append(str(IP_M))
                        elif i_count_spoof == 2:
                            PR_M = x_td.text
                            PR_List.append(str(PR_M))
                    i_count_spoof = 0
            return IP_List,PR_List
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
    
    def FIND_TRUE_PROXY():
        try:
            print("\n")
            sc_ip_list,sc_port_list = USER_OPS.PROXY_LIST()
            USER_OPS.USER_AGENT_LIST()
            user_agent_all = {"User-Agent":f"{random.choice(list_agent)}"}
            test_url_one = "https://ipinfo.io/json"
            x_stop_count = 0
            try:
                global true_prox_http,true_prox_https
                if x_stop_count == 0:
                    for x_ip,x_port in zip(sc_ip_list,sc_port_list):
                        try:
                            define_prx_dict = {"https":f"https://{str(x_ip)}:{str(x_port)}",
                                               "http":f"http://{str(x_ip)}:{str(x_port)}"}
                            rs = requests.Session()
                            att_req = rs.get(test_url_one,headers=user_agent_all,proxies=define_prx_dict,timeout=30)
                            if att_req.status_code == 200:
                                print("\n")
                                print("%s" % (PRINT_OPS.GREEN_ECHO("PROXY - FOUND")))
                                Json_Res = json.loads(att_req.text)
                                print(Json_Res["ip"])
                                print("COUNTRY ",Json_Res["country"])
                                print(Json_Res["org"])
                                print(Json_Res["timezone"])
                                true_prox_http = define_prx_dict["http"]
                                true_prox_https = define_prx_dict["https"]
                                print("HTTP: ",true_prox_http)
                                print("HTTPS: ",true_prox_https)
                                print("\n")
                                rs.close()
                                x_stop_count += 1
                                break
                            else:
                                rs.close()
                                pass
                        except:
                            print("%s" % (PRINT_OPS.YELLOW_ECHO("[i] PROXY SEARCHING")))
                print("\n")
            except:
                print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED")))
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))

    def GET_HEADER_EXAMPLE():
        try:
            global main_header
            USER_OPS.USER_AGENT_LIST()
            user_agent_all = random.choice(list_agent)
            ref_ex_list = USER_OPS.READING_FILE("ref_list.txt")
            ref_all = random.choice(ref_ex_list)
            date_day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month = ["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number = random.randint(1,30)
            date_year = random.randint(2000,2021)
            date_time_x = random.randint(10,23)
            date_time_y = random.randint(10,50)
            date_time_z = random.randint(10,55)
            keep_alive_rate = random.randint(100,155)
            main_header = {"User-Agent":str(user_agent_all),
                          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Connection":"Keep-Alive",
                          "Keep-Alive":str(keep_alive_rate),
                          "Content-Type":"text/html",
                          "Accept-Encoding":"gzip,deflate",
                          "Accept-Language":"en-us,en;q=0.5",
                          "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                          "Referer":str(ref_all),
                          "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("GETTING INFO FAILED, TRY AGAIN")))
            pass
        
    def W_REQ_OPS(target_url=str):
        try:
            global content_target,status_target
            if "https://" in target_url or "http://" in target_url:
                USER_OPS.GET_HEADER_EXAMPLE()
                USER_OPS.FIND_TRUE_PROXY()
                dict_proxies={"http":true_prox_http,
                              "https":true_prox_https}
                req_session = requests.session()
                req_connection = req_session.get(target_url,
                                                 headers=main_header,
                                                 timeout=22,
                                                 verify=False,
                                                 stream=True,
                                                 proxies=dict_proxies)
                content_target = req_connection.content
                status_target = req_connection.status_code
                req_connection.close()
            else:
                target_new = "http://"+target_url
                USER_OPS.GET_HEADER_EXAMPLE()
                USER_OPS.FIND_TRUE_PROXY()
                dict_proxies={"http":true_prox_http,
                              "https":true_prox_https}
                req_session = requests.session()
                req_connection = req_session.get(target_new,
                                                 headers=main_header,
                                                 timeout=22,
                                                 verify=False,
                                                 stream=True,
                                                 proxies=dict_proxies)
                content_target = req_connection.content
                status_target = req_connection.status_code
                req_connection.close()
        except:
            print("%s" % (PRINT_OPS.YELLOW_ECHO("PROXY CONNECTION DENIED,TRY AGAIN TO FIND A NEW PROXY")))
            pass
            
    def REQ_OPS(target_url=str):
        try:
            global content_target,status_target
            if "https://" in target_url or "http://" in target_url:
                USER_OPS.GET_HEADER_EXAMPLE()
                req_session = requests.session()
                req_connection = req_session.get(target_url,
                                                 headers=main_header,
                                                 timeout=22,
                                                 verify=False,
                                                 stream=True)
                content_target = req_connection.content
                status_target = req_connection.status_code
                req_connection.close()
            else:
                target_new = "http://"+target_url
                USER_OPS.GET_HEADER_EXAMPLE()
                req_session = requests.session()
                req_connection = req_session.get(target_new,
                                                 headers=main_header,
                                                 timeout=22,
                                                 verify=False,
                                                 stream=True)
                content_target = req_connection.content
                status_target = req_connection.status_code
                req_connection.close()
        except:
            print("%s" % (PRINT_OPS.RED_ECHO("CONNECTION ERROR, CHECK YOUR CONNECTION AND TRY AGAIN")))
            pass


def RUNNING_ALL():
    QT_F_RUN = OPTp(add_help_option=False,epilog="SUPERCOOKIE ESCAPE")
    QT_F_RUN.add_option("-p",
                        "--proxyrun",
                        type="string",
                        dest="x_proxy",
                        help="RUN PROCESS WITH PROXIES")
    QT_F_RUN.add_option("-r",
                        "--run",
                        type="string",
                        dest="x_run",
                        help="RUN PROCESS")
    QT_F_RUN.add_option("-h",
                        "--help",
                        action="store_true",
                        dest="x_help",
                        help="HELP")
    main_exp,arg_exp = QT_F_RUN.parse_args()
    if main_exp.x_proxy:
        user_ask = str(main_exp.x_proxy).replace(" ","")
        class RUNNING_W_PROXY():
            try:
                flask_app_one = Flask(__name__,template_folder="template")
                @flask_app_one.route("/")
                def root_index():
                    try:
                        USER_OPS.W_REQ_OPS(user_ask)
                        return content_target
                    except:
                        print("%s" % (PRINT_OPS.YELLOW_ECHO("INTERNAL ERROR,TRY AGAIN TO FIND A NEW PROXY")))
                        pass
                        
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("PROXY CONNECTION DENIED,TRY AGAIN TO FIND A NEW PROXY")))
                pass
            try:
                @flask_app_one.route("/next/<tar_site>")
                def additional_index(tar_site):
                    try:
                        USER_OPS.W_REQ_OPS(tar_site)
                        return content_target
                    except:
                        print("%s" % (PRINT_OPS.YELLOW_ECHO("INTERNAL ERROR,TRY AGAIN TO FIND A NEW PROXY")))
                        pass
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("PROXY CONNECTION DENIED,TRY AGAIN TO FIND A NEW PROXY")))
                pass
            try:
                with Controller.from_port() as controller:
                    controller.authenticate()
                    response_creation = controller.create_ephemeral_hidden_service({80:5000},
                                                                                    await_publication=True)
                    print("\n")
                    print(PRINT_OPS.YELLOW_ECHO("[>]"+"---"*7+"[<]"))
                    print(PRINT_OPS.GREEN_ECHO(response_creation.service_id+".onion"))
                    print(PRINT_OPS.YELLOW_ECHO("[>]"+"---"*7+"[<]"))
                    print("\n")
                    try:
                        flask_app_one.run(debug=False)
                    finally:
                        print("\n")
                        print(PRINT_OPS.RED_ECHO("[X]"+"---"*7+"[X]"))
                        print(PRINT_OPS.RED_ECHO("SERVER-DOWN"))
                        print(PRINT_OPS.RED_ECHO("[X]"+"---"*7+"[X]"))
                        print("\n")
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("TOR CONNECTION DENIED,CHECK YOUR PARAMETERS AND TRY AGAIN")))
                pass 
    elif main_exp.x_run:
        user_ask = str(main_exp.x_run).replace(" ","")
        class RUNNING_SIMPLE():
            try:
                flask_app = Flask(__name__,template_folder="template")
                @flask_app.route("/")
                def root_index():
                    try:
                        USER_OPS.REQ_OPS(user_ask)
                        return content_target
                    except:
                        print("%s" % (PRINT_OPS.YELLOW_ECHO("INTERNAL ERROR,TRY AGAIN TO FIND A NEW PROXY")))
                        pass
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("PROXY CONNECTION DENIED,TRY AGAIN TO FIND A NEW PROXY")))
                pass
            try:
                @flask_app.route("/next/<tar_site>")
                def additional_index(tar_site):
                    try:
                        USER_OPS.REQ_OPS(tar_site)
                        return content_target
                    except:
                        print("%s" % (PRINT_OPS.YELLOW_ECHO("INTERNAL ERROR,TRY AGAIN TO FIND A NEW PROXY")))
                        pass
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("PROXY CONNECTION DENIED,TRY AGAIN TO FIND A NEW PROXY")))
                pass
            try:
                with Controller.from_port() as controller:
                    controller.authenticate()
                    response_creation = controller.create_ephemeral_hidden_service({80:5000},
                                                                                    await_publication=True)
                    print("\n")
                    print(PRINT_OPS.YELLOW_ECHO("[>]"+"---"*7+"[<]"))
                    print(PRINT_OPS.GREEN_ECHO(response_creation.service_id+".onion"))
                    print(PRINT_OPS.YELLOW_ECHO("[>]"+"---"*7+"[<]"))
                    print("\n")
                    try:
                        flask_app.run(debug=False)
                    finally:
                        print("\n")
                        print(PRINT_OPS.RED_ECHO("[X]"+"---"*7+"[X]"))
                        print(PRINT_OPS.RED_ECHO("SERVER-DOWN"))
                        print(PRINT_OPS.RED_ECHO("[X]"+"---"*7+"[X]"))
                        print("\n")
            except:
                print("%s" % (PRINT_OPS.YELLOW_ECHO("TOR CONNECTION DENIED,CHECK YOUR PARAMETERS AND TRY AGAIN")))
                pass
    elif main_exp.x_help:
        USER_OPS.SHOW_INFO()
        pass
    else:
        USER_OPS.SHOW_INFO()
        pass
        
if __name__ == "__main__":
    try:
        RUNNING_ALL()
    except:
        USER_OPS.SHOW_INFO()
        pass
