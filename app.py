import web
import humanhash


urls = (
    '/(.*)', 'hash'
)

app = web.application(urls, globals())

class hash:        
    def GET(self, args):
        huuid = humanhash.uuid()[0] # generate humanhash, extract words, not UUID
        hhuid_sep = huuid.split("-") # split words
        hhash = "-".join(hhuid_sep[:2]).strip() + "\n" # two-word hash
        return hhash

if __name__ == "__main__":
    app.run()
