import csv, os
from django.conf import settings

from basehandler.models import IntervalData, Parameter, Company
from singleview.models import CompanyStatsFigure
def csv_handler(self, request, obj):
    
    if len(obj)>1:
        return self.message_user(request,"select any 1 file")
    
    obj = obj[0]

    if obj.data_file.name.split('.')[-1] != 'csv':
        return self.message_user(request,"Please upload csv file only.")
    
    try:
        file_name = os.path.join(settings.BASE_DIR, obj.data_file.name)
        csv_reader_fd = csv.reader( open( file_name,'rb' ) )
    except IOError as e:
        obj.status = 'Error'
        return self.message_user(request,"error in reading the file %s" %(e))
    else:
        interval_val = obj.interval
        header = csv_reader_fd.next()
        header_values_dict = dict(Parameter.objects.all().values_list('name', 'id'))
        company_values_dict = dict(Company.objects.all().values_list('name', 'id'))
        for each_row in csv_reader_fd:
            dataset_list = []
            mapped_param_val = zip(header[1:], each_row[1:])
            for each_param in mapped_param_val:
                if each_param[0] and each_param[1]:
                    _data_set = {'company_id' : company_values_dict.get(each_row[0])}
                    _data_set['param_id'] = header_values_dict.get(each_param[0])
                    _data_set['value'] = float(each_param[1])
                    _data_set['interval_id'] = interval_val.id
                    dataset_list.append(CompanyStatsFigure(**_data_set))
            CompanyStatsFigure.bulk_create_data(dataset_list)
        
        obj.status = 'Success.'
        obj.save()
        
        return self.message_user(request,"Successfully Uploaded.")



















    
    return 0
