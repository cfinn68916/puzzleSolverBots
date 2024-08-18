import subprocess
import time
import requests
import bs4


def pst():
    with requests.Session() as session:
        response = session.get('https://www.puzzle-binairo.com/?size=9')
        response.raise_for_status()
        a = bs4.BeautifulSoup(response.text, 'html.parser')
        param = ''
        b = ''
        w = ''
        h = ''
        size = ''

        for fld in a.find('form').find_all('input'):
            if 'name' in fld.attrs:
                if fld['name'] == 'param':
                    param = fld['value']
                if fld['name'] == 'b':
                    b = fld['value']
                if fld['name'] == 'w':
                    w = fld['value']
                if fld['name'] == 'h':
                    h = fld['value']
                if fld['name'] == 'size':
                    size = fld['value']
        task = response.text.split('var task = \'')[1].split('\'')[0]
        st=time.time()
        ad=subprocess.run(['./main_opt'],input=(task+'\n'+str(w)).encode(), capture_output=True)
        ans=ad.stdout.decode('ascii').strip('\n')

        res=session.post('https://www.puzzle-binairo.com/',data=[("param",param),("b",b),("w",w),("h",h),("size",size),("ansH",ans),("robot","1"),("ready","+++Done+++")])
        # print(res.text)
        res.raise_for_status()
        return task, ans

with open("q1000",'w') as f:
    with open("a1000", 'w') as f2:
        for i in range(1000):
            a=pst()
            f.write(a[0]+"\n")
            f2.write(a[1]+"\n")