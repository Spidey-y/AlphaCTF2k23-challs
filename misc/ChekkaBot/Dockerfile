FROM python:3.8

WORKDIR /bot

COPY challenge .

RUN pip3 install -r requirements.txt 

ENV TOKEN=MTA1NTEyNTE5MDI1NTg0OTUyMg.GS9Ksl.76vTak0DliM6oIXsg14qmVlsN5T7WMeUsQyEbM
ENV FLAG=AlphaCTF{D1Sc0rD_b07s_ArE_fun_JUsT_MAKE_SuRe_70_$eCur3_ThEm}

RUN adduser --disabled-password --force-badname alphaCTF
RUN  chmod 777 /bot/
USER alphaCTF


ENTRYPOINT ["python3", "-u", "main.py"]
