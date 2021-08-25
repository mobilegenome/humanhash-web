import web
import humanhash


urls = (
    '/(.+)', 'hash'
)

app = web.application(urls, globals())

def generate_human_hash():
    huuid = humanhash.uuid()[0] # generate humanhash, extract words, not UUID
    hhuid_sep = huuid.split("-") # split words
    hhash = "-".join(hhuid_sep[:2]).strip() + "\n" # two-word hash
    return hhash


class hash:
    def GET(self, args):
        output = []
        if not args.strip("/").endswith("hash"):
            try:
                n_hash = int(args.split("/")[-1])
                if n_hash > 0 and n_hash < 256:
                    for _ in range(n_hash):
                        output.append(generate_human_hash())
                else:
                    output.append("Out of parameter space")
            except ValueError as e:
                print(e)
                pass # not covertable
        else:
            output.append(generate_human_hash())
        return "".join(output)

if __name__ == "__main__":
    app.run()

