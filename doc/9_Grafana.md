# Grafana

<hr/>

[1. Grafana Setting](#grafana-setting)

[2. Monitoring Setting](#monitoring-setting)

<hr/>

## Grafana Setting

* Open web-browser and go `https://grafana.monitor.yemilab.kr` and login

### Connect InfluxDB to Grafana

* Click `Configuration` &rarr; `Data sources` &rarr; `Add data source`

<img src = "./images/grafana/grafana-01.png" width = "80%"></img>

* Select `InfluxDB`

<img src = "./images/grafana/grafana-02.png" width = "80%"></img>

1. Set Name
2. Select `Flux` for InfluxDB2
3. Fill InfluxDB URL : `https://influxdb.monitor.yemilab.kr`
4. Fill Grafana User name
5. Fill Organization
6. Fill telegraf token
7. Fill Bucket
8. Save

<img src = "./images/grafana/grafana-03.png" width = "80%"></img>

<img src = "./images/grafana/grafana-04.png" width = "80%"></img>

<img src = "./images/grafana/grafana-05.png" width = "80%"></img>

## Monitoring Setting

* Click `Dashboards` &rarr; `+ New dashboard`

<img src = "./images/grafana/grafana-06.png" width = "80%"></img>

* Add an empty panel

<img src = "./images/grafana/grafana-07.png" width = "80%"></img>

* Past script from [8_Telegraf](./8_telegraf.md)

