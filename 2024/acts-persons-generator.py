import csv
import html

actstemplate = ''
with open('act-template.html') as f:
	actstemplate = f.read()

personstemplate = ''
with open('person-template.html') as f:
	personstemplate = f.read()

actsfile = open('acts.tsv')
acts = csv.reader(actsfile, delimiter='\t')

personsfile = open('persons.tsv')
persons = csv.reader(personsfile, delimiter='\t')

def name_to_fn(name):
	return name.lower().replace(' ', '-')

for act in acts:
	out = actstemplate
	out = out.replace('TITLE', html.escape(act[1], True))
	persons_html = ''
	persons_list = act[2].split(', ')
	for person in persons_list:
		if len(persons_html):
			persons_html += ', '
		persons_html += '<a href="../persons/' + name_to_fn(person) + '.html">' + person + '</a>'
	out = out.replace('PERSONS', persons_html)
	proceedings_html = ''
	proceedings_list = act[4].split(', ')
	for proceeding in proceedings_list:
		if len(proceedings_html):
			proceedings_html += ', '
		if len(proceeding):
			proceedings_html += '<a href="' + proceeding + '" target="_blank">Entry in Proceedings</a>'
	out = out.replace('PROCEEDINGS', proceedings_html)
	video_html = ''
	if (len(act[5])):
		video_html += '<a href="https://www.youtube.com/watch?v=' + act[5] + '&list=PLQvkt3KblW27G-Rzym71PkIzJOCPTlueP" class="video"><img src="https://img.youtube.com/vi/' + act[5] + '/0.jpg"></a>';
	out = out.replace('VIDEO', video_html)
	description_nl = '<p>' + html.escape(act[3], True).replace('  ', '</p><p>') + '</p>'
	out = out.replace('DESCRIPTION', description_nl)
	f = open('program/' + act[0] + '.html', 'w')
	f.write(out)
	f.close()

for person in persons:
	out = personstemplate
	out = out.replace('REALNAME', html.escape(person[1], True))
	out = out.replace('NAME', html.escape(person[0], True))
	out = out.replace('AFFILIATION', html.escape(person[2], True))
	bio_nl = '<p>' + html.escape(person[3], True).replace('  ', '</p><p>') + '</p>'
	out = out.replace('BIO', bio_nl)
	f = open('persons/' + name_to_fn(person[0]) + '.html', 'w')
	f.write(out)
	f.close()
