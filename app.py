import web
import humanhash


urls = (
    '/hash', 'hash',
    '/hash/([0-9]*)', 'hash',  # set number of hashes to return
    '/hash/([0-9]*)/length/([1234]{1})', 'hash'  # set hash length
)

max_multi_hash = 256
app = web.application(urls, globals())

def generate_human_hash(n_words):
    huuid = humanhash.uuid()[0] # generate humanhash, extract words, not UUID
    hhuid_sep = huuid.split("-") # split words
    hhash = "-".join(hhuid_sep[:n_words]).strip() + "\n" # two-word hash
    return hhash


class hash:
    def GET(self, n_hash=1, length=2):
        output = []
        try:
            n_hash = int(n_hash)
            length = int(length)
            if n_hash > 0 and n_hash < max_multi_hash:
                for _ in range(n_hash):
                    output.append(generate_human_hash(n_words=length))
        except ValueError as e:
            print(e)
            pass # not covertable
        return "".join(output)

if __name__ == "__main__":
    app.run()

