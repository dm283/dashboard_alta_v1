# SELECTS FROM DATABASE

from functions_library import DB_NAME, DB_SCHEMA

select_query, select_columns = {}, {}
select_filter = {}
dashboard_filter_string = 'dashboard_filter_string'


s1 = 'product_quantity'
select_query[s1] = f"""
  SELECT count(*) product_quantity FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad
"""
select_filter[s1] = ''



s2 = 'dt_quantity'
select_query[s2] = f"""
  SELECT count(*) dt_quantity FROM (SELECT id_doc FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad GROUP BY id_doc) AS a
"""
select_filter[s2] = ''



s3 = 'tnved_quantity'
select_query[s3] = f"""
  select * from (
  SELECT TOP 7 * FROM
    (SELECT LEFT(g33_in,4) g33, count(*) cnt
    FROM {DB_NAME}.{DB_SCHEMA}.tovar_sklad  WHERE 1=1
    GROUP BY LEFT(g33_in,4)) AS a
    ORDER BY 2 DESC) b
    order by cnt
"""
select_filter[s3] = ''



s4 = 'products_on_storage'
select_query[s4] = f"""
  SELECT id,gtdnum,name, cast(date_in as date) date_in, g32,g31,g33_in,g31_2,
  CASE WHEN g41a <>'166' THEN g31_3 ELSE 0 END g31_3,
  CASE WHEN g41a <>'166' THEN g31_3a ELSE '' END g31_3a,
  g35,g41a, cast(date_chk as date) date_chk, country 
  FROM {DB_NAME}.{DB_SCHEMA}.TOVAR_SKLAD 
  ORDER BY date_in ASC,gtdnum,g32
"""
select_filter[s4] = ''



###

s5 = 'received_product_quantity'
select_query[s5] = f"""
  SELECT count(*) received_product_quantity
    FROM {DB_NAME}.{DB_SCHEMA}.doc_in_sklad d, {DB_NAME}.{DB_SCHEMA}.doc_in_sklad_sub s 
    WHERE s.main_id=d.id AND d.posted > 0
    {dashboard_filter_string}
"""
# select_filter[s5] = "and d.date_doc >='dashboard_filter_0_0' AND d.date_doc <= 'dashboard_filter_0_1'"
select_filter[s5] = list()
select_filter[s5].append("and d.date_doc >='dashboard_filter_0_0'")
select_filter[s5].append("and d.date_doc <= 'dashboard_filter_0_1'")



s6 = 'received_dt_quantity'
select_query[s6] = f"""
  SELECT count(*) received_dt_quantity
    FROM {DB_NAME}.{DB_SCHEMA}.doc_in_sklad d
    WHERE posted > 0
    {dashboard_filter_string}
"""
# select_filter[s6] = "and d.date_doc >='dashboard_filter_0_0' AND d.date_doc <= 'dashboard_filter_0_1'"
select_filter[s6] = list()
select_filter[s6].append("and d.date_doc >='dashboard_filter_0_0'")
select_filter[s6].append("and d.date_doc <= 'dashboard_filter_0_1'")



s7 = 'received_tnved_quantity'
select_query[s7] = f"""
  SELECT TOP 7 * FROM
  (SELECT  LEFT(s.g33_in,4) g33, count(*) cnt 
    FROM {DB_NAME}.{DB_SCHEMA}.doc_in_sklad_sub s, {DB_NAME}.{DB_SCHEMA}.doc_in_sklad d  
    where s.main_id=d.id AND d.posted > 0
    {dashboard_filter_string}
    GROUP BY LEFT(s.g33_in,4)) AS a
  ORDER BY 2 DESC
"""
# select_filter[s7] = "and d.date_doc >='dashboard_filter_0_0' and d.date_doc <= 'dashboard_filter_0_1'"
select_filter[s7] = list()
select_filter[s7].append("and d.date_doc >='dashboard_filter_0_0'")
select_filter[s7].append("and d.date_doc <= 'dashboard_filter_0_1'")


s8 = 'account_book'
select_query[s8] = f"""
  SELECT * FROM 
  (SELECT UniqueIndexField as id, id as id_0, f_p,name,gtdnum, cast(date_in as date) date_in, time_in,
  cast(date_otc as date) date_otc, cast(date_chk as date) date_chk, g32,g31,g33_in,g35,
  CASE WHEN g31_3a <>'КГ' THEN g31_3 ELSE 0 END g31_3,
  CASE WHEN g31_3a <>'КГ' THEN g31_3a ELSE '' END g31_3a,
  doc_num_out, gtdregime_out, cast(date_out as date) date_out, g32_out, g33_out, g31_2_out, g35_out,
  CASE WHEN g31_3a <>'КГ' THEN g31_3_out ELSE 0 END g31_3_out
  FROM {DB_NAME}.{DB_SCHEMA}.jr_sklad ) AS a
  where 1=1
  {dashboard_filter_string}
  ORDER BY date_in,id ASC,g32 ASC,f_p DESC,date_otc ASC
"""
# select_filter[s8] = "and date_in >='dashboard_filter_1_0' and date_in <= 'dashboard_filter_1_1'"
select_filter[s8] = list()
select_filter[s8].append("and date_in >='dashboard_filter_1_0'")
select_filter[s8].append("and date_in <= 'dashboard_filter_1_1'")



###

s9 = 'report_vehicle'
select_query[s9] = f"""
SELECT nn as id, gtdnum,g32,g33_in,g31,
CAST(g35 AS NUMERIC(18,3)) g35,
g31_3a,place,gtdregime_out,doc_num_out,g33_out,
CAST(g35_out AS NUMERIC(18,3)) g35_out,
CASE WHEN g31_3a <> 'КГ' THEN CAST(CAST(g31_3 AS NUMERIC(18,3)) AS VARCHAR)+'/'+g31_3a ELSE '0' END g31_3, 
CASE WHEN g31_3a <> 'КГ' THEN CAST(CAST(g31_3_out AS NUMERIC(18,3)) AS VARCHAR)+'/'+g31_3a ELSE '0' END g31_3_out, 
CONVERT(VARCHAR,date_in,105) AS date_in,
CONVERT(VARCHAR,date_chk,105) AS date_chk,
CASE WHEN exp_date IS NOT NULL THEN CONVERT(VARCHAR,exp_date,105) ELSE 'ОТСУТСТВУЕТ' END AS exp_date,
CONVERT(VARCHAR,date_out,105) AS date_out,
CASE WHEN g31_3ost>0 THEN CAST(g35ost AS NUMERIC(18,3)) ELSE 0 END g35ost_,
CASE WHEN g31_3a <> 'КГ' THEN CAST(CAST(g31_3ost AS NUMERIC(18,3)) AS VARCHAR)+'/'+g31_3a ELSE '0' END g31_3ost_ 
FROM (SELECT CONVERT(INTEGER,row_number() OVER( ORDER BY j.date_in,j.id,j.g32,j.key_id,jj.date_out)) nn,j.*,
   jj.date_out,jj.doc_num_out,jj.gtdregime_out,
   jj.g35_out,jj.g31_3_out,jj.g31_3a_out,jj.g31_out,jj.g32_out,jj.g33_out,j.g31_3-ISNULL(jjj.g31_3sout,0) g31_3ost,
   g35-ISNULL(jjj.g35sout,0) g35ost 
FROM (SELECT j.id,j.key_id,j.g32,j.gtdnum,j.date_in,j.g31,j.g31_3,j.g31_3a,j.g33_in,j.g35,j.gtdregime_in,j.date_chk,
   j.place,s.exp_date,s.g41a_dt,u.code 
FROM ({DB_NAME}.{DB_SCHEMA}.jr_sklad j LEFT OUTER JOIN {DB_NAME}.{DB_SCHEMA}.units u ON u.name10=j.g31_3a) 
LEFT OUTER JOIN {DB_NAME}.{DB_SCHEMA}.doc_in_sklad_sub s ON s.key_id=j.key_id 
WHERE f_p='1' {dashboard_filter_string}) j LEFT OUTER JOIN (SELECT key_id,sum(g35_out) 
   g35sout,sum(g31_3_out) g31_3sout 
FROM {DB_NAME}.{DB_SCHEMA}.jr_sklad jj WHERE f_p='0' GROUP BY key_id ) jjj ON jjj.key_id=j.key_id 
LEFT OUTER JOIN (SELECT key_id,doc_num_out,gtdregime_out,date_out,g31_3_out,g31_3a_out,g35_out,g31_out,g32_out,g33_out 
FROM {DB_NAME}.{DB_SCHEMA}.jr_sklad WHERE  f_p='0') jj  ON j.key_id=jj.key_id ) AS a WHERE 1=1
ORDER BY nn
"""

select_filter[s9] = list()
select_filter[s9].append("and date_out >='dashboard_filter_2_0'")
select_filter[s9].append("and date_in <= 'dashboard_filter_2_1'")


###############################################################
# s1 = 'web_service_usage'
# select_query[s1] = f"""
#       select id, web_service, user_id, device, country, user_status, sign_date, signout_date
#         from {DB_NAME}.{DB_SCHEMA}.web_service_usage
#         where user_status = 'sign_in'
#         order by sign_date desc
# """
# select_columns[s1] = ['id', 'web_service', 'user_id', 'device', 'country', 'user_status', 'sign_date', 'signout_date']


# s2 = 'telegram_chats'
# # select_query[s2] = f"""
# #       select id, chat_id, entity_name, bot_name, update_date 
# #         from {DB_NAME}.{DB_SCHEMA}.telegram_chats
# #         where is_active = 1
# # """
# select_query[s2] = f"""
#       select id, chat_id, entity_name, bot_name, update_date 
#         from {DB_NAME}.{DB_SCHEMA}.telegram_chats
#         where is_active
# """
# select_columns[s2] = ['id', 'chat_id', 'entity_name', 'bot_name', 'update_date']


# s3 = 'telegram_messages'
# select_query[s3] = f"""
#       select uniqueindexfield, adrto, attachmentfiles, datep, dates 
#         from {DB_NAME}.{DB_SCHEMA}.telegram_messages
# """
# select_columns[s3] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


# s4 = 'email_messages'
# select_query[s4] = f"""
#       select uniqueindexfield, adrto, attachmentfiles, datep, dates 
#         from {DB_NAME}.{DB_SCHEMA}.uemail
# """
# select_columns[s4] = ['uniqueindexfield', 'adrto', 'attachmentfiles', 'datep', 'dates']


# s5 = 'count_messages'
# select_query[s5] = f"""
#   select count(uniqueindexfield) as msg_cnt, 'email' as channel
#     from {DB_NAME}.{DB_SCHEMA}.uemail
#   union all
#   select count(uniqueindexfield) as cnt, 'telegram' as channel
#     from {DB_NAME}.{DB_SCHEMA}.telegram_messages
# """
# select_columns[s5] = ['msg_cnt', 'channel']


# s6 = 'count_telegram_chats_types'
# select_query[s6] = f"""
#   select entity_type, count(id) as chat_cnt
#     from {DB_NAME}.{DB_SCHEMA}.telegram_chats
#     group by entity_type
# """
# select_columns[s6] = ['entity_type', 'chat_cnt']


# s7 = 'messages_email'
# select_query[s7] = f"""
#   select id, adrto, subj, textemail, attachmentfiles, datep, dates from {DB_NAME}.{DB_SCHEMA}.messages_email
# """
# select_columns[s7] = ['id', 'adrto', 'subj', 'textemail', 'attachmentfiles', 'datep', 'dates']


# s8 = ''
# select_query[s8] = f"""
# select id, adrto, subj, dates from {DB_NAME}.{DB_SCHEMA}.messages_telegram
# """
# select_columns[s8] = ['id', 'adrto', 'subj', 'dates']
