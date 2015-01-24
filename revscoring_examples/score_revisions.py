"""
This script applies the IsContentRule scorer to revisions.

Usage:
	score_revisions <revid>... --api=<url>

Options:
	<revid>      A revision identifier
	--api=<url>  The base URL for a mediawiki API
"""
import docopt
from mw.api import Session
from revscores.extractors import APIExtractor
from revscores.features import is_mainspace
from revscores.languages import english

from .adds_foo import AddsFooRule

def main():
	args = docopt.docopt(__doc__)
	
	extractor = APIExtractor(Session(args['--api']), language=english)
	
	scorer = AddsFooRule(extractor)
	
	rev_ids = [int(r) for r in args['<revid>']]
	
	for score in scorer.score(rev_ids):
		print(score)


