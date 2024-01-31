class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.selectFields = []
        self.conditions = []
        self.order_by_field = None
        self.order_by_direction = None
        self.limit_value = None
        self.offset_value = None

    def select(self, *fields):
        self.selectFields.extend(fields)
        return self
    def where(self, field, operator, value):
        self.conditions.append((field, operator, value))
        return self

    def orderBy(self, field, direction='asc'):
        self.order_by_field = field
        self.order_by_direction = direction
        return self

    def limit(self, value):
        self.limit_value = value
        return self

    def offset(self, value):
        self.offset_value = value
        return self

    def buildQuery(self):
        query = f"SELECT {', '.join(self.selectFields)} FROM {self.table}"

        if self.conditions:
            conditions = ' AND '.join(f"{field} {operator} '{value}'" for field, operator, value in self.conditions)
            query += f" WHERE {conditions}"

        if self.order_by_field:
            query += f" ORDER BY {self.order_by_field} {self.order_by_direction.upper()}"

        if self.limit_value:
            query += f" LIMIT {self.limit_value}"

        if self.offset_value:
            query += f" OFFSET {self.offset_value}"

        return query

    def insert(self, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        return f"INSERT INTO {self.table} ({columns}) VALUES ({values})"

    def update(self, data):
        values = ', '.join(f"{key} = '{value}'" for key, value in data.items())
        if self.conditions:
            conditions = ' AND '.join(f"{field} {operator} '{value}'" for field, operator, value in self.conditions)
            return f"UPDATE {self.table} SET {values} WHERE {conditions}"
        else:
            raise ValueError("Update query must have at least one condition.")

    def delete(self):
        if self.conditions:
            conditions = ' AND '.join(f"{field} {operator} '{value}'" for field, operator, value in self.conditions)
            return f"DELETE FROM {self.table} WHERE {conditions}"
        else:
            raise ValueError("Delete query must have at least one condition.")