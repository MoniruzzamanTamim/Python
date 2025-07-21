



command = ""
car_start =False
car_stop = False

while command != "exit":
        command = input("Enter command: ")
        try :
                if command == "start":
                        if car_start:
                                car_stop = True
                                print("Car already Started.....")
                        else:
                                car_start = True
                                car_stop = True
                                print("Car is Started")
                elif command == "stop":
                        if car_stop:
                                car_stop = False
                                car_start = False
                                print("Car is Stopped")
                        else:
                                car_start = False
                                print("Car already Stopped.....")
                elif command == "restart":
                        print("Car is Restarted...........")
                elif command == "help":
                        print('''
                                        start = Car is Start
                                        stop= car is stop
                                        help= show all commands
                                        exit = Game is Over
                                        restart = Game is Restart
                                ''')
                elif command == "exit":
                        print("Program IS Exit 'Enjoy Your Life'")
                        break
                else:
                        print("Invalid Command 'NEED a HELP Please Type:  help' ")
        except Exception as  e:
                print({e})
        

