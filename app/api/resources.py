from flask import request
from flask_restplus import Resource
import humanize

from . import api_rest
from .homer.analyzer import Article


@api_rest.route('/stats')
class StatsResource(Resource):
    @staticmethod
    def get_stats(text):
        article = Article('', '', text=text)
        summary = {}
        for attr in ('total_paragraphs', 'avg_sentences_per_para', 'len_of_longest_paragraph', 'total_sentences', 'avg_words_per_sentence', 'len_of_longest_sentence', 'total_words'):
            summary[attr] = getattr(article, attr)

        summary['reading_time'] = humanize.naturaldelta(article.total_words / 6.66)
        summary['flesch_reading'] = article.get_flesch_reading_score()
        summary['dale_chall'] = article.get_dale_chall_reading_score()
        summary['longest_sentence'] = '{}...'.format(str(article.longest_sentence)[0:30])
        if article.total_words:
            summary['and_frequency'] = round(article.total_and_words / article.total_words * 100, 2)

        summary['compulsive_hedgers'] = ', '.join(str(hedger) for hedger in article.get_compulsive_hedgers())
        summary['intensifiers'] = ', '.join(str(hedger) for hedger in article.get_intensifiers())
        summary['vague_words'] = ', '.join(str(hedger) for hedger in article.get_vague_words())

        paragraphs = []
        for item, para in enumerate(article.paragraphs, start=1):
            paragraphs.append({
                'number': item,
                'total_sentences': len(para),
                'total_words': para.total_words,
                'avg_words_per_sentence': para.avg_words_per_sentence,
                'longest_sentence': '{}...'.format(str(para.longest_sentence)[0:30]),
                'flesch_reading': para.get_flesch_reading_score(),
                'dale_chall': para.get_dale_chall_reading_score()
            })

        return {'summary': summary, 'paragraphs': paragraphs}

    def post(self):
        json_payload = request.json
        self.get_stats(json_payload['text'])
        stats = self.get_stats(json_payload['text'])
        return stats, 200
