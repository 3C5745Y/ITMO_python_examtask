import pandas as pd
import json
import datetime as dt

try:
    with open('base.json') as my_file:
        json_date = json.load(my_file)
    df = pd.DataFrame(json_date)
    flag = 1
except:
    flag = 0

num = None

while num != 0 :
    print("""
                Hello 
                
                1. Add
                2. Show all
                3. Show for date 
                4. Show by category
                5. Show by min -> max
                6. Delete 
                0. Exit
                            """)
    try:
        num = int(input("What would you like to do?: "))

        if num == 0:
            if flag == 1:
                with open('base.json') as f:
                    text = f.read()
                if len(text) < 1:
                    break
                else:
                    df.to_json('base.json')
                    break
            else:
                break
        if num == 1:

            cat = input("Введите категорию: ")
            prod = input("Введите объект: ")
            price = input("Введите цену: ")
            date = input("Введите дату в формате 'YYYY-MM-DD': ")

            with open('base.json') as f:
                text = f.read()

            if len(text) < 1:
                file = open("base.json", "w")
                str = '{"Category":{"0":"' + cat + '"},"Product":{"0":"' + prod +'"},"Cost":{"0":' + price + '},"Date":{"0":"' + date + '"}}'
                file.write(str)
                file.close()
                with open('base.json') as my_file:
                    json_date = json.load(my_file)
                df = pd.DataFrame(json_date)
                flag = 1
            else:
                series = pd.Series({"Category": cat, "Product": prod, "Cost": int(price), "Date": date})
                df = df.append(series, ignore_index=True)
                df.to_json('base.json')

        if num == 2:
            try:
                with open('base.json') as my_file:
                    json_date = json.load(my_file)
                df = pd.DataFrame(json_date)
                print(df)
            except:
                print("Файлов нет")
        if num == 3:
            try:
                with open('base.json') as my_file:
                    json_date = json.load(my_file)
                df = pd.DataFrame(json_date)
                print(df['Date'])
                date = input("Выберите дату в формате 'YYYY-MM-DD': ")
                df_show = df[df["Date"] == date]
                print(df_show)
            except:
                print("Файлов нет")
        if num == 4:
            try:
                with open('base.json') as my_file:
                    json_date = json.load(my_file)
                df = pd.DataFrame(json_date)
                category = input("Введите категорию: ")
                df_show = df[df["Category"] == category]
                print(df_show)
            except:
                print("Файлов нет")
        if num == 5:
            try:
                with open('base.json') as my_file:
                    json_date = json.load(my_file)
                df = pd.DataFrame(json_date)
                print(df.sort_values('Cost'))
            except:
                print("Файлов нет")
        if num == 6:
            f = open('base.json', 'w')
            f.close()
    except (TypeError, ValueError):
        print("That didn't look like an integer to me.")
    except Exception as e:
        print(e)



