# coding:utf8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open('output.html','a')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # res_data["info_url"] = info_url
        # res_data["info_photo_url"] = info_photo_url
        # res_data["info_name"] = info_name
        # res_data["info_price"] = info_price
        # res_data["info_description"] = info_description

        for data in self.datas:
            fout.write("</tr>")
            fout.write("<td>%s</td>" % (data['info_url']).encode('utf-8'))
            # fout.write("<td>%s</td>" % (data['info_photo_url']).encode('utf-8'))
            fout.write("<td>%s</td>" % (data['info_name']).encode('utf-8'))
            fout.write("<td>%s</td>" % (data['info_price']).encode('utf-8'))
            fout.write("<td>%s</td>" % (data['info_description']).encode('utf-8'))
            # fout.write("<td>%s</td>"%(data['url']))
            # fout.write("<td>%s</td>" % (data['title']).encode('utf-8'))
            # fout.write("<td>%s</td>" % (data['summary']).encode('utf-8'))
            fout.write("</tr>")
            fout.write("</tr>")
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")