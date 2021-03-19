
sources=$(wildcard */*.md)
htmls=$(subst .md,.html,$(sources))
targets=$(htmls)

all: $(targets)

clean:
	rm -f $(targets)



%.html: head.txt  %.md
	cat  $^  | pandoc  > $@


