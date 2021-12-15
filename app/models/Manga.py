class Manga:
    def __init__(self, name: str, url_img: str, nb_sold: int) -> None:
        """
            Constructeur de la classe Manga
        Args:
            name (str): Nom du manga
            url_img (str): Url de l'image scan du manga
            nb_sold (int): Nombre d'exemplaire vendu
        """
        self.name = name
        self.url_img = url_img
        self.nb_sold = nb_sold

    @staticmethod
    def to_dict(name: str, url_img: str, nb_sold: int) -> dict:
        """
            Retourne un dictionnaire avec les données passées en paramètre
        Args:
            name (str): Nom du manga
            url_img (str): Url de l'image scan du manga
            nb_sold (int): Nombre d'exemplaire vendu

        Returns:
            dict: Dictionnaire avec les données passés en paramètre
        """
        return dict(name=name, url_img=url_img, nb_sold=nb_sold)