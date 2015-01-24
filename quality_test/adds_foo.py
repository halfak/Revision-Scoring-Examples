from revscores.scorers import Scorer
from revscores.features import Feature
from revscores.datasources import contiguous_segments_added

def process_add_foo(contiguous_segments_added):
	for segment in contiguous_segments_added:
		if 'foo' in segment or 'Foo' in segment: return True
	
	return False

adds_foo = Feature("adds_foo", process_add_foo, depends_on=[contiguous_segments_added], returns=bool)


class AddsFooRule(Scorer):
	
	def score(self, rev_ids):
		
		for rev_id in rev_ids:
			feature_values = self.extractor.extract(rev_id, [adds_foo])
			af = feature_values[0]
			yield {"adds_foo": af}
