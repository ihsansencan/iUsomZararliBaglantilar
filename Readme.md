# # iUsomZararliBaglantilar

## Zararlı bağlantı Listesine USOM sitesinden ulaşabilirsiniz.

`wget https://usom.gov.tr/url-list.txt`

```
root@ihsan:~/Desktop# wc -l url-list.txt
90183 url-list.txt
```
03.02.2021 tarihli listemizde.
`56 adet site çift yazılmış...`
`Toplamda: 90.127 site bulunuyor.`

## Zararlı Bağlantı Ara.

```python
root@ihsan:~/Desktop# python3 ZararliBaglantiAra.py

***************************
* #UsomZararliBaglantilar *
* @IhsanSencan            *
***************************

Aranacak Kelime: pandemidestekbasvurusu
pandemidestekbasvurusu.com
pandemidestekbasvurusu.com : 195.142.1.93
saglikbakanligi-pandemidestekbasvurusu.com
e-devlet-pandemidestekbasvurusuindir.com
e-devlet-pandemidestekbasvurusuapp.com
turkiyegov-pandemidestekbasvurusu.com
turkiyeonline-pandemidestekbasvurusu.com
eturkiye-pandemidestekbasvurusu.com
eturkiye-pandemidestekbasvurusu.com : 104.21.47.80
pandemidestekbasvurusu.tk
pandemidestekbasvurusu.tk : 185.176.43.102
root@ihsan:~/Desktop# 
```