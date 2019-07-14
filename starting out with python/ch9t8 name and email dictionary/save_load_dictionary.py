import pickle


def pickle_it(emails):
    with open('addresses.txt', 'wb') as output_file:
        pickle.dump(emails, output_file)


def unpickle_it():
    with open('addresses.txt', 'ab+') as input_file:
        try:
            emails = pickle.load(input_file)
        except:
            emails = {}
        return emails
