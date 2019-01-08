log = []
person = None
with open('3.txt', 'r', encoding='UTF-8-SIG') as f:
    for line in f:
        log.append(line.strip().split(' ',1))
for line in log:
    t = line[0][:5]
    p = line[0][5:]
    if p == 'Allen':
        person = 'Allen'
    elif p == 'Viki':
        person = 'Viki'
    if person:
        print(person, ':', line[1], '@', t)
# # define function
# def read_file(filename):
#     log = []
#     with open(filename, 'r', encoding='UTF-8-SIG') as f:
#         for line in f:
#             log.append(line.strip())
#     return log
# def formatting(log):
#     formated = []
#     person = None
#     a_wd_cnt = 0
#     a_sticker_cnt = 0
#     a_img_cnt = 0
#     v_wd_cnt = 0
#     v_sticker_cnt = 0
#     v_img_cnt = 0
#     for line in log:
#         formated = line.split(' ', 2)
#         t = formated[0]
#         p = formated[1]
#         s = formated[2]
#         if p == 'Allen':
#             if s == '貼圖':
#                 a_sticker_cnt += 1
#             elif s == '圖片':
#                 a_img_cnt += 1
#             else:
#                 for sentence in s:
#                     a_wd_cnt += len(sentence)
#         elif p == 'Viki':
#             if s == '貼圖':
#                 v_sticker_cnt += 1
#             elif s == '圖片':
#                 v_img_cnt += 1
#             else:
#                 for sentence in s:
#                     v_wd_cnt += len(sentence)
# #    return formated
#     print('Allen typed', a_wd_cnt, 'words.')
#     print('Allen sent', a_sticker_cnt, 'stickers.')
#     print('Allen sent', a_img_cnt, 'images.')
#     print('Viki typed', v_wd_cnt, 'words.')
#     print('Viki sent', v_sticker_cnt, 'stickers.')
#     print('Viki sent', v_img_cnt, 'images.')

# def write_file(outputname, formated):
#     with open(outputname, 'w', encoding='UTF-8') as f:
#         f.write('time,name,content\n')
#         for line in formated:
#             f.write(line[0] + ',' + line[1] + ',' + line[2] + '\n')

# # define main function
# def main():
#     filename = '3.txt' # input('Which log do you want to input? ')
#     log = read_file(filename)
#     formated = formatting(log)
# # run main function
# if __name__ == '__main__':
#     main()