all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
	hfst-invert chv.gen.hfst > chv.mor.hfst
	echo -e "source chv.stem.regex\nsave stack chv.stem.hfst\nhyvästi" | hfst-xfst 
	hfst-substitute -i chv.lexc.hfst -o chv.lexc_guesser.hfst  -f '🂡:🂡' -T chv.stem.hfst
	hfst-compose-intersect -1 chv.lexc_guesser.hfst -2 chv.twol.hfst -o chv.gen_guesser.hfst

clean:
	rm *.hfst
