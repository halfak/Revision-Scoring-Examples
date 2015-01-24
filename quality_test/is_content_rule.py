from revscores.scorers import Scorer
from revscores.features import is_content_namespace

class IsContentRule(Scorer):
	
	def score(self, rev_ids):
		
		for rev_id in rev_ids:
			feature_values = self.extractor.extract(rev_id, [is_content_namespace])
			icn = feature_values[0]
			yield {"is_content": icn}
