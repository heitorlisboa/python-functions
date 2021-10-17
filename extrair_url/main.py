from iter_to_dictionary import iter_to_dictionary


class ExtratorUrl:
    def __init__(self, url):
        self.url = url
        self.__url_separado = self.__separar_url()

    def __str__(self):
        return self.url

    def __len__(self):
        return len(self.url)

    @property
    def base(self):
        if type(self.__url_separado) == str:
            return self.__url_separado
        else:
            return self.__url_separado[0]

    @property
    def parametros_juntos(self):
        if type(self.__url_separado) == str:
            return None
        else:
            return self.__url_separado[1]

    @property
    def parametros_separados(self):
        if type(self.__url_separado) == str or not self.__url_separado[2]: # AQUI!!!
            return None
        else:
            return self.__url_separado[2]

    def __separar_url(self):
        separador = self.url.find('?')
        if separador == -1:
            return self.url
        else:
            url_base = self.url[:separador]
            url_parametros_juntos = self.url[separador+1:]
            url_parametros_separados = self.__separar_parametros(url_parametros_juntos)
            return url_base, url_parametros_juntos, url_parametros_separados

    @staticmethod
    def __separar_parametros(url_parametros):
        lista_parametros = []
        while True:
            index_pre_parametro = url_parametros.find('=')
            if index_pre_parametro == -1:  # Se NÃO houver parâmetro
                dicionario_parametros = iter_to_dictionary(lista_parametros)
                return dicionario_parametros  # Único lugar onde vai retornar o valor
            else:  # Se houver parâmetro
                index_e_comercial = url_parametros.find('&')
                if index_e_comercial == -1:  # Se NÃO houver MAIS DE UM parâmetro
                    lista_parametros.append([url_parametros[:index_pre_parametro],
                                             url_parametros[index_pre_parametro+1:]])
                    url_parametros = ''
                else:  # Se houver MAIS DE UM parâmetro
                    lista_parametros.append([url_parametros[:index_pre_parametro],
                                             url_parametros[index_pre_parametro+1:index_e_comercial]])
                    url_parametros = url_parametros[index_e_comercial+1:]


if __name__ == '__main__':

    minha_url = ExtratorUrl('https://www.google.com/search?client=opera-gx&q=pesquisa+de+teste&sourceid=opera&ie=UTF-8&oe=UTF-8')
    # minha_url = ExtratorUrl('https://www.youtube.com/results?search_query=pesquisa+de+teste')
    # minha_url = ExtratorUrl('https://www.youtube.com')
    # minha_url = ExtratorUrl('palavras?aleatorias')

    print(f'URL Completa: {minha_url}\n')
    print(f'URL Base: {minha_url.base}\n')
    print(f'Parâmetros juntos: {minha_url.parametros_juntos}\n')
    print(f'Parâmetros separados: {minha_url.parametros_separados}')
