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
	if args:
		try:
			n_hash = int(args)
			if n_hash > 0 and n_hash < 256:
				for _ in range(n_hash):
					output.append(generate_human_hash())

		except ValueError:
			# not covertable
			pass
	else:
		output.append(generate_human_hash())
        return "\n".join(output)

if __name__ == "__main__":
    app.run()
