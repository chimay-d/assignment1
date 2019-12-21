import urllib.request

url2id = {}

class URL_Shortener:
    # suppose, we already have 10 billion urls
    id = 10000000000
    # store url to id in order not to have duplicated url with different id
    
    
    def shorten_url(self, original_url):
        if original_url in url2id:
            id = url2id[original_url]
            shorten_url = self.encode(id)
        else:
            # store url2id in order not to have duplicated url with different id in the future
            url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            # increase cnt for next url
            self.id += 1
        
        return "short_url.com/"+shorten_url
    
    def encode(self, id):
        # base 62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        # convert base10 id into base62 id for having alphanumeric shorten url
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        # since ret has reversed order of base62 id, reverse ret before return it
        return "".join(ret[::-1])

    def open(self, id) :
        for key in url2id.items() :
            if url2id[key] == id :
                webUrl  = urllib.request.urlopen(url2id[id])
                print ("result code: " + str(webUrl.getcode()))
                data = webUrl.read()
                print (data)


shortener = URL_Shortener()


def main() :
    print("1. Enter url and get shortened url: ")
    print("2. Enter shortened url to open url: ")
    print('3. Exit')
    ch = input("Enter your choice: ")
    ch = int(ch)
    while ch != 3 :
        if ch == 1 :
            org_url = input("Enter original url:")
            print(shortener.shorten_url(org_url))
        elif ch == 2 :
            srt_url = input("Enter short url: ")
            shortener.open(srt_url)

        ch = input('Enter your choice: ')
        ch = int(ch)

if __name__ == "__main__":
    main()
