import random

while True:
    true = True
    coach_unsorted = []
    sorted_coach_name = []
    coach_unsorted_hr = []
    coach_sorted_hr = []

    # Admin Functionalities

    def input_coach():
        coach_data = open("coachdata.txt", "a")
        coach1id = input("\nCoach ID(ex : CO1234) : ")
        coach1name = str(input("Coach Name : ")).lower()
        coach1dj = input("Coach Joined(dd/mm/yyyy) : ")
        coach1hr = input("Coach Hourly Rate(ex : 123 RM) : ")
        coach1phone = input("Coach Phone Number(ex : 07654321) : ")
        coach1add = input("Coach Address : ")
        spccode = input("Enter sport centre ID(ex : SC0000) : ")
        spcname = input("Enter sport centre name : ")
        spcode = input("Enter sport ID (ex : SP0000) : ")
        spname = input("Enter sport assigned to coach : ")
        coach_data.write("\n" + coach1id + "\t" + coach1name + "\t" + coach1dj + "\t" +
                         coach1hr + "\t" + coach1phone + "\t" + coach1add + "\t" + "-" + "\t" + spccode + "\t" +
                         spcname + "\t" + spcode + "\t" + spname + "\t" + "-" + "\t" + "0" + "\t" + "-")
        coach_data.close()

    def input_sport():
        sport_data = open("sportdata.txt", "a")
        sportid = input("Enter Sport ID(ex : SP0000) : ")
        sportcentid = input("Enter sport centre ID(ex : SC0000) : ")
        sportname = input("Enter Sport Name : ")
        sportcoach = input("Coach name assigned to the sport : ")
        sportcentname = input("Enter sport centre name : ")
        sport_data.write("\n" +
            sportid + "\t" + sportcentid + "\t" + sportname + "\t" + sportcentname + "\t" + sportcoach)
        sport_data.close()

    def input_sport_schedule():
        sport_schedule = open("sportschedule.txt", "a")
        sportid = input("Enter sport ID (ex : SP0000): ")
        sportname = input("Enter sport name : ")
        sportcentid = input("Enter sport centre ID : ")
        sportcentname = input("Enter sport centre name : ")
        sportday = input("Enter sport day : ")
        sporttime = input("Enter sport time (ex : 19:00) : ")
        sport_schedule.write("\n" + sportid + "\t" + sportcentid + "\t" + sportcentname + "\t" + sportday + "\t" + sporttime + "\t" + sportname + "\n")
        sport_schedule.close()

    def input_student_record():
        student_login_data = open("studentusepass.txt", "a")
        student_name = input("Enter your name : ")
        student_dob = input("Enter your date of birth(dd/mm/yyyy) : ")
        student_email = input("Enter your email address : ")
        student_phone = input("Enter your phone number : ")
        student_address = input("Enter you address : ")
        student_sport = input("Enter your sport : ")
        student_username = input("Enter your chosen username : ")
        student_pass = input("Enter your chosen password : ")
        student_id = random.randrange(1000, 10000)
        s_id = "ST" + str(student_id)

        student_login_data.write("\n" + student_username + "\t" +student_pass)
        student_login_data.close()

        student_self_data = open("studentdata.txt", "a")
        student_self_data.write(
            "\n" + student_username + "\t" + s_id + "\t" + student_name + "\t" + student_sport + "\t" + student_dob +
            "\t" + student_email + "\t" + student_phone + "\t" + student_address + "\t" + student_pass + "\n")
        student_self_data.close()

    def display_coach():
        print("=============================================================================================================================================")
        print("Coach ID|Coach Name|Date Joined|Hourly Rate|Phone Number|Address|Terminated Date|SPC ID|SPC Name|SP ID|SP Assigned|Rating|Total|latest rating")
        coach_data = open("coachdata.txt", "r")
        print(coach_data.read())
        coach_data.close()

    def student_self_records():
        student_data = open("studentdata.txt", "r")
        for display_check in student_data:
            display_check = display_check.strip()
            if display_check.startswith(student_log_use) and display_check.endswith(student_log_pass):
                print("===============================================================================================================================")
                print("Student Username|Student ID|Student Name|Student sport|Student DOB|Student Email|Student Phone|Student Address|Student Password")
                print(display_check)
        student_data.close()

    def display_student():
        print("=================================================================================================================")
        print("Student Username|Student ID|Student Name|Student DOB|Student Email|Student Phone|Student Address|Student Password")
        student_data = open("studentdata.txt", "r")
        print(student_data.read())
        student_data.close()

    def display_sport():
        print("====================================================================")
        print("Sport ID|Sport Centre ID|Sport Name|Assigned coach|Sport Centre Name")
        sport_data = open("sportdata.txt", "r")
        print(sport_data.read())
        sport_data.close()

    def display_schedule():
        print("==========================================================================")
        print("Sport ID|Sport Centre ID|Sport Centre Name|Sport Day|Sport Time|Sport Name")
        schedule_data = open("sportschedule.txt", "r")
        print(schedule_data.read())
        schedule_data.close()

    def display_self_schedule():
        student_self_records()
        display_sport()
        sched_data = open("sportschedule.txt", "r")
        sidname = input("Enter your sport ID : ")
        sname = input("Enter your sport name : ")
        for self_check in sched_data:
            if self_check.startswith(sidname) and self_check.endswith(sname):
                print("==========================================================================")
                print("Sport ID|Sport Centre ID|Sport Centre Name|Sport Day|Sport Time|Sport Name")
                print(self_check)

    def sort_coach_name():
        coach_data = open("coachdata.txt", "r")
        t = coach_data.readlines()

        readd = open("coachdata.txt", "r")
        cnt = 0
        rline = readd.read()
        rlines = rline.split("\n")
        for x in rlines:
            if x:
                cnt += 1

        cnt2 = -1
        for ccc in range(cnt):
            el = t[cnt2 + 1].split("\t")
            el[0], el[1] = el[1], el[0]
            coach_unsorted.append(el)
            cnt2 += 1

        while coach_unsorted:
            early = coach_unsorted[0]
            for sorting_coach in coach_unsorted:
                if sorting_coach < early:
                    early = sorting_coach
            sorted_coach_name.append(early)
            coach_unsorted.remove(early)

            print(*sorted_coach_name, sep="\n")

            sorted_coach_name.clear()

    def sort_coach_payrate():
        coach_sortpay = open("coachdata.txt", "r")
        m = coach_sortpay.readlines()

        new = open("coachdata.txt", "r")
        countt = 0
        line = new.read()
        lines = line.split("\n")
        for i in lines:
            if i:
                countt += 1

        countt2 = -1
        for z in range(countt):
            c = m[countt2 + 1].split("\t")
            c[0], c[3] = c[3], c[0]
            coach_unsorted_hr.append(c)
            countt2 += 1

        while coach_unsorted_hr:
            early1 = coach_unsorted_hr[0]
            for sorting_coach1 in coach_unsorted_hr:
                if sorting_coach1 < early1:
                    early1 = sorting_coach1
            coach_sorted_hr.append(early1)
            coach_unsorted_hr.remove(early1)

            print(*coach_sorted_hr, sep="\n")

            coach_sorted_hr.clear()

    def sort_coach_rating():
        coach_sort = open("coachdata.txt", "r")
        m = coach_sort.readlines()

        new = open("coachdata.txt", "r")
        countt = 0
        line = new.read()
        lines = line.split("\n")
        for i in lines:
            if i:
                countt += 1

        countt2 = -1
        for z in range(countt):
            c = m[countt2 + 1].split("\t")
            c[0], c[11] = c[11], c[0]
            coach_unsorted_hr.append(c)
            countt2 += 1

        while coach_unsorted_hr:
            early1 = coach_unsorted_hr[0]
            for sorting_coach1 in coach_unsorted_hr:
                if sorting_coach1 < early1:
                    early1 = sorting_coach1
            coach_sorted_hr.append(early1)
            coach_unsorted_hr.remove(early1)

        print(*coach_sorted_hr, sep="\n")

        coach_sorted_hr.clear()

    def modify_coach():
        coach_modif = open("coachdata.txt", "r")
        m = coach_modif.readlines()
        ''' aaa
            bbb
            ccc
            [[a,a,a], [b,b,b], ccc]'''

        checker = True
        while checker:
            print("====================================================================================================")
            no = 0
            for numbering in m:
                print((no + 1), ".", numbering.strip())
                no += 1
            try:
                print('==================================================================================================')
                x = int(input("Enter which number you want to modify : "))
                n = m[x-1].split("\t")

                while True:
                    print("\n1. Coach ID : ", n[0])
                    print("2. Coach Name : ", n[1])
                    print("3. Date Joined : ", n[2])
                    print("4. Coach Hourly Rate : ", n[3])
                    print("5. Coach Phone Number : ", n[4])
                    print("6. Coach Adress : ", n[5])
                    print("7. Date Terminated : ", n[6])
                    print("8. Sport Centre ID : ", n[7])
                    print("9. Sport Centre Name : ", n[8])
                    print("10. Sport ID : ", n[9])
                    print("11. Sport Assigned : ", n[10])

                    modif = input("\nWhich part you want to modify?")

                    if modif.lower() == "id" or modif.lower() == "coach id" or modif == "1":
                        n[0] = input("Please reenter coach id : ")
                    elif modif.lower() == "name" or modif.lower() == "coach name" or modif == "2":
                        n[1] = input("Please reenter name : ").lower()
                    elif modif.lower() == "date joined" or modif.lower() == "joined" or modif == "3":
                        n[2] = input("Please reenter coach date join : ")
                    elif modif.lower() == "coach hourly rate" or modif.lower() == "hourly rate" or modif == "4":
                        n[3] = input("Please reenter coach hourly rate : ")
                    elif modif.lower() == "coach phone number" or modif.lower() == "phone number" or modif == "5":
                        n[4] = input("Please reenter coach phone number : ")
                    elif modif.lower() == "coach address" or modif.lower() == "address" or modif == "6":
                        n[5] = input("Please reenter address : ")
                    elif modif.lower() == "date terminated" or modif.lower() == "terminated" or modif == "7":
                        n[6] = input("Please reenter date terminated : ")
                    elif modif.lower() == "sport centre id" or modif.lower() == "sport id" or modif == "8":
                        n[7] = input("Please reenter sport centre id : ")
                    elif modif.lower() == "sport centre name" or modif.lower() == "sport name" or modif == "9":
                        n[8] = input("Please reenter sport centre name : ")
                    elif modif.lower() == "sport id" or modif == "10":
                        n[9] = input("Please reenter sport ID : ")
                    elif modif.lower() == "sport assigned" or modif == "11":
                        n[10] = input("Please reenter sport assigned : ")
                    else:
                        print("\nInvalid input, please try again.\n")
                        continue

                    update = "\t".join(n)
                    m[x-1] = update

                    with open("coachdata.txt", "w") as q:
                        q.writelines(m)
                        q.close()

                    print("Record has been updated")
                    checker = False
                    break
            except ValueError:
                print("\ninput must be integer\n")
            except IndexError:
                print("\nPlease input a valid number\n")

    def modify_sport():
        sport_modif = open("sportdata.txt", "r")
        s = sport_modif.readlines()

        cek = True
        while cek:
            print("====================================================================================================")
            num = 0
            for menumber in s:
                print((num + 1), ".", menumber.strip())
                num += 1

            try:
                print("====================================================================================================")
                a = int(input("Enter which number you want to modify : "))
                b = s[a-1].split("\t")

                while True:
                    print("1. Sport ID : ", b[0])
                    print("2. Sport Centre ID : ", b[1])
                    print("3. Sport Name  : ", b[2])
                    print("4. Assigned Coach: ", b[3])
                    print("5. Sport Centre Name : ", b[4])

                    modif2 = input("Which part you want to modify : ")

                    if modif2.lower() == "sport id" or modif2 == "1":
                        b[0] = input("Please reenter sport ID : ")
                    elif modif2.lower() == "sport centre id" or modif2.lower() == "centre id" or modif2 == "2":
                        b[1] = input("Please reenter sport centre id : ")
                    elif modif2.lower() == "sport name" or modif2 == "3":
                        b[2] = input("Please reenter sport name : ")
                    elif modif2.lower() == "assigned coach" or modif2.lower() == "coach" or modif2 == "4":
                        b[3] = input("Please reenter coach assigned to sport : ")
                    elif modif2.lower() == "sport centre name" or modif2.lower() == "centre name" or modif2 == "5":
                        b[4] = input("PLease reenter sport centre name : ")
                    else:
                        print("Invalid input, please try again")
                        continue

                    updating = "\t".join(b)
                    s[a-1] = updating

                    with open("sportdata.txt", "w") as v:
                        v.writelines(s)
                        v.close()

                    print("Record has been updated")
                    cek = False
                    break

            except ValueError:
                print("\nInput must be integer, please try again.\n")
            except IndexError:
                print("\nPlease input a valid number\n")

    def modify_sport_schedule():
        schedule_modif = open("sportschedule.txt", "r")
        r = schedule_modif.readlines()

        cekk = True
        while cekk:
            print(
                "====================================================================================================")
            numm = 0
            for menumb in r:
                print((numm + 1), ".", menumb.strip())
                numm += 1

            try:
                print(
                    "====================================================================================================")
                w = int(input("Enter which number you want to modify : "))
                e = r[w - 1].split("\t")

                while True:
                    print("1. Sport ID : ", e[0])
                    print("2. Sport name : ", e[5])
                    print("3. Sport centre ID : ", e[1])
                    print("4. Sport centre name : ", e[2])
                    print("5. Sport day : ", e[3])
                    print("6. Sport time : ", e[4])

                    modif3 = input("Which part you want to modify : ")
                    if modif3.lower() == "sport id" or modif3 == "1":
                        e[0] = input("Please reenter sport ID : ")
                    elif modif3.lower() == "sport name" or modif3 == "2":
                        e[5] = input("Please reenter sport name : ")
                    elif modif3.lower() == "sport centre id" or modif3.lower() == "centre id" or modif3 == "3":
                        e[1] = input("Please reenter sport centre id : ")
                    elif modif3.lower() == "sport centre name" or modif3.lower() == "centre name" or modif3 == "4":
                        e[2] = input("Please reenter sport centre name : ")
                    elif modif3.lower() == "sport day" or modif3.lower() == "day" or modif3 == "5":
                        e[3] = input("PLease reenter sport day : ")
                    elif modif3.lower() == "sport time" or modif3.lower() == "time" or modif3 == "6":
                        e[4] = input("Please reenter sport time : ")
                    else:
                        print("\nInvalid input, please try again.\n")
                        continue

                    updatee = "\t".join(e)
                    r[w - 1] = updatee

                    with open("sportschedule.txt", "w") as k:
                        k.writelines(r)
                        k.close()

                    print("Record has been updated")
                    cekk = False
                    break

            except ValueError:
                print("\nInput must be integer, please try again.\n")
            except IndexError:
                print("\nPlease input a valid number\n")

    def input_rating():
        coach_rate = open("coachdata.txt", "r")
        rl1 = coach_rate.readlines()

        checking = True
        while checking:
            print("=====================================================================================================")
            hit = 0
            for counting in rl1:
                print((hit + 1), ".", counting.strip())
                hit += 1

            try:
                print(
                    "========================================================================================================")
                rrll = int(input("Enter which number you want to rate : "))
                rl2 = rl1[rrll - 1].split("\t")

                while True:
                    print("Coach rating : ", rl2[11])
                    print("Total review : ", rl2[12])

                    rateee = float(input("Please enter rating (1-5) : "))

                    if rateee <= 5 and rateee >= 1:
                        rl2[12] = str(int(rl2[12]) + 1)
                        if rl2[11] == "-":
                            avg = rateee
                        else:
                            avg = ((float(rl2[11]) * (float(rl2[12]) - 1)) + float(rateee)) / float(rl2[12])
                        rl2[13] = str(rateee) + "\n"
                        rl2[11] = str(avg)

                        updating = "\t".join(rl2)
                        rl1[rrll - 1] = updating

                        with open("coachdata.txt", "w") as aaa:
                            aaa.writelines(rl1)
                            aaa.close()

                        checking = False
                        break
                    else:
                        print("\nInvalid input, please try again\n")
                        continue
            except ValueError:
                print("\nPlease input an integer\n")
            except IndexError:
                print("\nPlease input a valid number\n")

    def modify_self_record():
        student_data = open("studentdata.txt", "r")
        dataaa = student_data.readlines()

        ter = 0
        for display_check in dataaa:
            if student_log_use in display_check:
                break
            else:
                ter += 1

        lineee = dataaa[ter].split("\t")
        while True:
            student_self_records()
            print("\nPlease enter number you want to modify")
            print("======================================")
            print("1. Modify Username")
            print("2. Modify name")
            print("3. Modify sport")
            print("4. Modify DOB")
            print("5. Modify email")
            print("6. Modify phone")
            print("7. Modify Password")
            print("8. Modify address")
            choice_student = input("Please enter choice : ")
            if choice_student == "2" or choice_student.lower() == "name":
                lineee[2] = input("Please reenter name : ")
            elif choice_student == "3" or choice_student.lower() == "sport":
                lineee[3] = input("Please reenter sport : ")
            elif choice_student == "1" or choice_student.lower() == "username":
                lineee[0] = input("Please reenter username : ")
            elif choice_student == "4" or choice_student.lower() == "dob":
                lineee[4] = input("Please reenter DOB : ")
            elif choice_student == "5" or choice_student.lower() == "email":
                lineee[5] = input("Please reenter email : ")
            elif choice_student == "6" or choice_student.lower() == "phone number":
                lineee[6] = input("Please reenter phone number : ")
            elif choice_student == "7" or choice_student.lower() == "password":
                lineee[8] = input("Please reenter password : ")
            elif choice_student == "8" or choice_student.lower() == "address":
                lineee[7] = input("Please reenter address : ")
            else:
                print("Invalid input, please try again.")
                continue

            update = "\t".join(lineee)
            dataaa[ter] = update

            with open("studentdata.txt", "w") as jk:
                jk.writelines(dataaa)
                jk.close()

            print("\nRecord has been updated")
            break

    # User Interface

    print("\nWelcome to Real Champions Sports Academy System")
    print("===============================================")
    print("1. Admin")
    print("2. Student")
    print("3. Exit")

    menu = input("\nMenu : ")

    if menu.lower() == "admin" or menu == "1":
        while true:
            cont_check = input("\nDo you want to continue?(Yes/No)")
            if cont_check.lower() == "yes":
                print("\nAdmin Login")
                print("===========")
                adm_user = input("Username : ")
                adm_pass = input("Password : ")
                if adm_user == "abcde" and adm_pass == "12345":
                    while True:
                        print("\nAdmin Function")
                        print("===============")
                        print("1. Register Records")
                        print("2. Display Records")
                        print("3. Search Records")
                        print("4. Sorted Records")
                        print("5. Modify records")
                        print("6. Exit")
                        adm_menu = input("\nAdmin : ")
                        if adm_menu == "1" or adm_menu.lower() == "register records":
                            while True:
                                print("\nWhat do you want to register?")
                                print("=============================")
                                print("1. Coach")
                                print("2. Sport")
                                print("3. Sport Schedule")
                                print("4. Exit")
                                adm_input1 = input("\nMenu : ")
                                if adm_input1 == "1" or adm_input1.lower() == "coach":
                                    m = True
                                    while m:
                                        no = 0
                                        input_coach()
                                        while True:
                                            check1 = input("\nDo You Want To Register Another Coach?(Y/N)")
                                            if check1.lower() == "y":
                                                print("Registering Another Coach")
                                                break
                                            elif check1.lower() == "n":
                                                print("Coach Registered")
                                                m = False
                                                break
                                            else:
                                                print("Please Answer With Y/N")

                                elif adm_input1.lower() == "sport" or adm_input1 == "2":
                                    m = True
                                    while m:
                                        input_sport()
                                        while True:
                                            check1 = input("\nDo You Want To Register Another Sport?(Y/N)")
                                            if check1.lower() == "y":
                                                print("Registering Another Sport\n")
                                                break
                                            elif check1.lower() == "n":
                                                print("Sport Registered\n")
                                                m = False
                                                break
                                            else:
                                                print("Please Answer With Y/N")

                                elif adm_input1.lower() == "sport schedule" or adm_input1 == "3":
                                    m = True
                                    while m:
                                        input_sport_schedule()
                                        while True:
                                            check1 = input("\nDo You Want To Register Another Sport Schedule?(Y/N)")
                                            if check1.lower() == "y":
                                                print("Registering Another Sport Schedule")
                                                break
                                            elif check1.lower() == "n":
                                                print("Schedule Registered")
                                                m = False
                                                break
                                            else:
                                                print("Please Answer With Y/N")
                                elif adm_input1.lower() == "exit" or adm_input1 == "4":
                                    break
                                else:
                                    print("Please Try Again.")

                        elif adm_menu == "2" or adm_menu.lower() == "display records":
                            while True:
                                print("\nWhat do you want to display?")
                                print("============================")
                                print("1. Coach")
                                print("2. Sport")
                                print("3. Registered Student")
                                print("4. Exit")
                                displaying = input("\nMenu : ")
                                if displaying == "1" or displaying.lower() == "coach":
                                    try:
                                        display_coach()
                                    except FileNotFoundError:
                                        print("No coach data found, please check your data.")
                                elif displaying == "2" or displaying.lower() == "sport":
                                    try:
                                        display_sport()
                                    except FileNotFoundError:
                                        print("No sport data found, please check your data.")
                                elif displaying == "3" or displaying.lower() == "registered student":
                                    try:
                                        display_student()
                                    except FileNotFoundError:
                                        print("No registered student data found")
                                elif displaying == "4" or displaying.lower() == "exit":
                                    break
                                else:
                                    print("Invalid input, please try again")

                        elif adm_menu == "3" or adm_menu.lower() == "search records":
                            while True:
                                print("\nWhat do you want to search?")
                                print("===========================")
                                print("1. Coach by detail(ID/name/rating/etc.)")
                                print("2. Sport ID")
                                print("3. Student ID")
                                print("4. Exit")
                                search = input("Enter your choice : ")
                                if search == "1" or search.lower() == "coach by detail":
                                    c = True
                                    display_coach()
                                    while c:
                                        count = 0
                                        print("===============================================================================\n")
                                        data_coach = input("Enter coach data : ")
                                        search_coach = open("coachdata.txt")
                                        for coachdt in search_coach:
                                            coachdt = coachdt.rstrip()
                                            if data_coach in coachdt:
                                                count += 1
                                                print(coachdt)
                                        if count == 0:
                                            print("Data not found")

                                        while True:
                                            retry = input("Do you want to search another coach?(Y/N)")
                                            if retry.lower() == "y":
                                                break
                                            elif retry.lower() == "n":
                                                c = False
                                                break
                                            else:
                                                print("Please answer with Y/N")
                                elif search == "2" or search.lower() == "sport id":
                                    c = True
                                    display_sport()
                                    while c:
                                        count = 0
                                        print("================================================================================\n")
                                        data_id = input("Enter sport id : ")
                                        search_id = open("sportdata.txt", "r")
                                        for sportid in search_id:
                                            if sportid.startswith(data_id):
                                                count += 1
                                                print(sportid)
                                        if count == 0:
                                            print("ID not found")
                                        while True:
                                            retry = input("Do you want to search another sport?(Y/N)")
                                            if retry.lower() == "y":
                                                break
                                            elif retry.lower() == "n":
                                                c = False
                                                break
                                            else:
                                                print("Please answer with Y/N")
                                elif search == "3" or search.lower() == "student id":
                                    c = True
                                    display_student()
                                    while c:
                                        count = 0
                                        print("===============================================================================\n")
                                        stu_detail = input("Enter student detail : ")
                                        stu_search = open("studentdata.txt")
                                        for stdetail in stu_search:
                                            stdetail = stdetail.rstrip()
                                            if stu_detail in stdetail:
                                                count += 1
                                                print(stdetail)
                                        if count == 0:
                                            print("data not found")
                                        while True:
                                            retry = input("Do you want to search another student?(Y/N)")
                                            if retry.lower() == "y":
                                                break
                                            elif retry.lower() == "n":
                                                c = False
                                                break
                                            else:
                                                print("Please answer with Y/N")
                                elif search == "4" or search.lower() == "exit":
                                    break
                                else:
                                    print("Invalid input, please try again.")

                        elif adm_menu.lower() == "sorted records" or adm_menu == "4":
                            while True:
                                print("\nWhat do you want to sort and display?")
                                print("=====================================")
                                print("1. Coach by name")
                                print("2. Coach by hourly rate")
                                print("3. Coach by rating")
                                print("4. Exit")
                                sorting = input("Enter your choice : ")

                                if sorting == "1" or sorting.lower() == "coach by name":
                                    sort_coach_name()
                                elif sorting == "2" or sorting.lower() == "coach by hourly rate":
                                    sort_coach_payrate()
                                elif sorting == "3" or sorting.lower() == "coach by rating":
                                    sort_coach_rating()
                                elif sorting == "4" or sorting.lower() == "exit":
                                    break
                                else:
                                    print("Invalid input, please try again.")

                        elif adm_menu.lower() == "modify records" or adm_menu == "5":
                            while True:
                                print("\nModify Records")
                                print("===============")
                                print("1. Coach")
                                print("2. Sport")
                                print("3. Sport Schedule")
                                print("4. Exit")
                                modify = input("Enter your choice : ")
                                if modify.lower() == "coach" or modify == "1":
                                    x = True
                                    while x:
                                        modify_coach()
                                        while True:
                                            recheck = input("Do you want to modify another coach(Yes/No)")
                                            if recheck.lower() == "yes":
                                                break
                                            elif recheck.lower() == "no":
                                                x = False
                                                break
                                            else:
                                                print("Please enter with yes/no")
                                elif modify.lower() == "sport" or modify == "2":
                                    x = True
                                    while x:
                                        modify_sport()
                                        while True:
                                            recheck = input("Do you want to modify another sport(Yes/No)")
                                            if recheck.lower() == "yes":
                                                break
                                            elif recheck.lower() == "no":
                                                x = False
                                                break
                                            else:
                                                print("Please enter with yes/no")

                                elif modify.lower() == "sport schedule" or modify == "3":
                                    x = True
                                    while x:
                                        modify_sport_schedule()
                                        while True:
                                            recheck = input("Do you want to modify another schedule(Yes/No)")
                                            if recheck.lower() == "yes":
                                                break
                                            elif recheck.lower() == "no":
                                                x = False
                                                break
                                            else:
                                                print("Please enter with yes/no")
                                elif modify.lower() == "exit" or modify == "4":
                                    break
                                else:
                                    print("\nInvalid input, please try again.")

                        elif adm_menu.lower() == "exit" or adm_menu == "6":
                            true = False
                            break
                        else:
                            print("Invalid input, please try again.")
                else:
                    print("\nPassword or Username Incorrect, Please Try Again.")
            elif cont_check.lower() == "no":
                print("getting you back to menu\n")
                break
            else:
                print("Please answer with yes/no.")

    elif menu.lower() == "student" or menu == "2":
        print("Student login")
        student_login_check = input("Are you a registered student?(yes/no)")
        if student_login_check.lower() == "no":
            while True:
                print("\nWelcome, guest student")
                print("======================")
                print("1. View sports")
                print("2. View Sport schedule")
                print("3. Register")
                print("4. Exit")
                guest_student = input("Enter your choice : ")
                if guest_student == "1" or guest_student.lower() == "view sports":
                    try:
                        display_sport()
                    except FileNotFoundError:
                        print("No data found")
                elif guest_student == "2" or guest_student.lower() == "view sport schedule":
                    try:
                        display_schedule()
                    except FileNotFoundError:
                        print("No data found")
                elif guest_student == "3" or guest_student.lower() == "register":
                    input_student_record()
                elif guest_student == "4" or guest_student.lower() == "exit":
                    break
                else:
                    print("Invalid input, please try again")

        elif student_login_check.lower() == "yes":
            func3 = True
            while func3:
                count2 = 0
                check2 = input("\nDo you want to continue?(yes/no)")
                if check2.lower() == "yes":
                    print("\n===========")
                    student_log_use = input("Username : ")
                    student_log_pass = input("Password : ")
                    student_check = open("studentdata.txt", "r")
                    for checking_student in student_check:
                        checking_student = checking_student.strip()
                        if checking_student.startswith(student_log_use) and checking_student.endswith(student_log_pass):
                            count2 += 1
                            while True:
                                print("\nHello, student")
                                print("==============")
                                print("1. View details of")
                                print("2. Modify Self Records")
                                print("3. Provide feedback and rating")
                                print("4. Exit")
                                logined_student = input("Enter your choice : ")
                                if logined_student == "1" or logined_student.lower() == "view details of":
                                    while True:
                                        print("\nWhat do you want to see the details of")
                                        print("========================================")
                                        print("1. Coach")
                                        print("2. Self record")
                                        print("3. Registered sport schedule")
                                        print("4. Exit")
                                        student_check1 = input("Enter your choice : ")
                                        if student_check1 == "1" or student_check1.lower() == "coach":
                                            display_coach()
                                        elif student_check1 == "2" or student_check1.lower() == "self record":
                                            student_self_records()
                                        elif student_check1 == "3" or student_check1.lower() == "registered sport schedule":
                                            display_self_schedule()
                                        elif student_check1 == "4" or student_check1.lower() == "exit":
                                            break
                                        else:
                                            print("Invalid input, please try again")
                                elif logined_student == "2" or logined_student.lower() == "modify self records":
                                    modify_self_record()
                                elif logined_student == "3" or logined_student.lower() == "provide feedback and rating":
                                    checkkk = True
                                    while checkkk:
                                        input_rating()
                                        while True:
                                            checkinggg = input("Do you want to rate another coach?(Y/N)")
                                            if checkinggg.lower() == "y":
                                                print("\n")
                                                checkkk = True
                                                break
                                            elif checkinggg.lower() == "n":
                                                checkkk = False
                                                break
                                            else:
                                                print("Please answer with y/n")
                                elif logined_student == "4" or logined_student.lower() == "exit":
                                    func3 = False
                                    break
                                else:
                                    print("Invalid input, please try again.")
                    if count2 == 0:
                        print("\nPassword or username incorrect, please try again.")
                    student_check.close()
                elif check2.lower() == "no":
                    break
                else:
                    print("\nInvalid input, please try again.")

        else:
            print("\nInvalid input, please answer with yes/no")

    elif menu.lower() == "exit" or menu == "3":
        break
    else:
        print("\nInvalid Input, Please Try Again.")
