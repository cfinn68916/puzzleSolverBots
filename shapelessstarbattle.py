import subprocess
import time
import requests
import bs4


def pst():
    with requests.Session() as session:
        response = session.get('https://www.puzzle-star-battle.com/?size=13')
        # session.cookies.set('api_token', 'NmG4oWK8XPBfoOnACvF11ZGsUJ00GkmVkZJw6lkdreS5nkKOXOoO1WGGNAe3')
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
        ad=subprocess.run(['./ShapelessStarBattle'],input=(task+'\n'+str(w)+"\n1").encode(), capture_output=True)
        ans=ad.stdout.decode('ascii').strip('\n')

        res=session.post('https://www.puzzle-star-battle.com/',data=[("param",param),("b",b),("w",w),("h",h),("size",size),("ansH",ans),("robot","1"),("ready","+++Done+++")])
        par=res.text.split('solparams" value="')[1].split('"')[0]
        print(par)
        # open("res.html",'w').write(res.text)

        # a=session.post('https://www.puzzle-star-battle.com/hallsubmit.php',data=[("solparams",par),("robot","1")])
        a=session.post('https://www.puzzle-star-battle.com/hallsubmit.php',data=[("solparams",par),("robot","1"),("email","cfinn68916@gmail.com"),("submitscore","1")])
        # open("asdf.html",'w').write(a.text)
        res.raise_for_status()
        print(a.status_code)
        return task, ans

for i in range(10):
    pst()