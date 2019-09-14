GROUP_BY_CHOICES = ('date', 'country', 'channel', 'os')

ORDER_BY_CHOICES = ('date', 'country', 'channel', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue')


class OrderByTypes:
    ASC = 'asc'
    DESC = 'desc'

    @staticmethod
    def choices():
        return OrderByTypes.ASC, OrderByTypes.DESC
