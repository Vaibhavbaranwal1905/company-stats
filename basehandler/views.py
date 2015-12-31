import re
import urllib
import pandas as pd
import base64
import pylab
import StringIO
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext
from django.template.response import TemplateResponse
from scipy.stats import stats
from basehandler.models import Company, IntervalData
from utility.utils import execute_raw_query,sort_dict_alphanumeric_keys
# Create your views here.

def fetch_data_list(*args):
    fetched_data = []
    _len_of_args = len(args)
    for each in args:
        _val_list = each.objects.all().order_by('id').values_list('id', 'name')
        fetched_data.append(_val_list)
    if _len_of_args == 1:
        fetched_data = fetched_data[0]
    return fetched_data


def get_image_uri_from_plot(plt):
    fig = plt.gcf()
    imgdata = StringIO.StringIO()
    fig.savefig(imgdata, format='png')
    imgdata.seek(0)  # rewind the data
    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    return uri

class HomePage(View):
    def get(self, request):
        return render(request, 'index.html',)

class CompanyRating(View):
    def get(self, request):
        company_list, interval_list = fetch_data_list(Company, IntervalData)
        return TemplateResponse(request, 'company_rating.html', locals())

    def post(self, request):
        company_list, interval_list = fetch_data_list(Company, IntervalData)
        company_val = request.POST.get('company')
        interval_val = request.POST.get('interval')
        if not any([company_val,interval_val]):
            err_message = 'Please select atleast one filter for results.'
            return TemplateResponse(request, 'company_rating.html', locals())
        company_rating_data = fetch_company_rating(company_val, interval_val)
        return TemplateResponse(request, 'company_rating.html', locals())

class CompanyStatistics(View):
    def get(self, request):
        company_list = fetch_data_list(Company)
        return TemplateResponse(request, 'company_stats.html', locals())

    def post(self, request):
        company_list = fetch_data_list(Company)
        company_val = request.POST.get('company')
        graph_type = request.POST.get('graph_type', 'barchart')
        if not company_val:
            err_message = 'Please select atleast one filter for results.'
            return TemplateResponse(request, 'company_stats.html', locals())
        company_rating_data = fetch_company_rating(company_val, '', 'id', True)
        crs = self.month_wise_company_relative_score(company_rating_data, company_val)
        crs = OrderedDict( sorted( crs.items(), key = sort_dict_alphanumeric_keys ) )
        graph_image = self.plot_graph_image(crs, graph_type)
        return TemplateResponse(request, 'company_stats.html', locals())
   
    def plot_graph_image(self,data_set, graph_type='barchart'):
        data_set = pd.DataFrame.from_dict(data_set, orient='index')
        if graph_type == 'barchart':
            data_set.plot(kind='bar',stacked=True,legend=None,title="Company Relative Score")
        else:
            data_set.plot(legend=None,title="Company Relative Score")
        #interval_name = np.array(data_set.keys())
        #relative_score = np.array(data_set.values())
        #pylab.figure(1)
        #x = range(len(data_set.keys()))
        #pylab.xticks(x, interval_name)
        #pylab.plot(x, relative_score)
        #pylab.tight_layout()
        image_html = get_image_uri_from_plot(plt)
        return image_html



    def month_wise_company_relative_score(self, data, company_val):
        company_val = int(company_val)
        interval_dict = dict(fetch_data_list(IntervalData))
        crs_dataset = {}
        for e_id,e_name in interval_dict.items():
            percentile_of_score = 0.0
            filtered_data = map(lambda x: (list(x).pop(0),float(list(x).pop(2))), filter(lambda x: x[1]==e_id , data))
            filtered_data_dict = dict(filtered_data)
            if filtered_data_dict.has_key(company_val):
                company_rating = filtered_data_dict[company_val]
                del filtered_data_dict[company_val]
                percentile_of_score = stats.percentileofscore(filtered_data_dict.values(), company_rating, kind='mean')
            crs_dataset[e_name] = round(percentile_of_score, 2)
        return crs_dataset

def fetch_company_rating(company_val = '', interval_val = '' , data_type = 'name', no_where = False):
        _query = '''
                select %s 
                from singleview_companystatsfigure csf 
                left join basehandler_parameter p on p.id=csf.param_id 
                left join basehandler_company c on c.id=csf.company_id 
                left join basehandler_intervaldata i on i.id=csf.interval_id 
                %s group by csf.company_id,csf.interval_id;
                '''
        if data_type == 'name':
            _fetched_data = 'c.name, i.name, FORMAT(sum(value*p.weightage)/sum(p.weightage), 2)'
        else:
            _fetched_data = 'c.id, i.id, FORMAT(sum(value*p.weightage)/sum(p.weightage), 2)'

        _where_clause = ' where '
        if company_val:
            _where_clause += ' csf.company_id = %s ' % company_val
        
        if interval_val:
            _where_clause += ' csf.interval_id = %s ' % interval_val
        
        if company_val and interval_val:
            _where_clause = ' where csf.company_id = %s and csf.interval_id = %s ' % (company_val, interval_val)
        
        if no_where:
            _where_clause = ''
        
        _query = _query % (_fetched_data, _where_clause)
        company_rating_data = execute_raw_query(_query)
        return company_rating_data
