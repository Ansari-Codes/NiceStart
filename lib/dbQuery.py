class Query:
    def __init__(self, table: str):
        self.table = table
        self._action = None
        self._columns = []
        self._values = {}
        self._where = []
        self._limit = None
        self._order_by = None

    # --- INSERT ---
    def insert(self, **data):
        self._action = "insert"
        self._values = data
        return self

    # --- SELECT ---
    def select(self, *columns):
        self._action = "select"
        self._columns = columns or ["*"]
        return self

    # --- UPDATE ---
    def update(self, **data):
        self._action = "update"
        self._values = data
        return self

    # --- DELETE ---
    def delete(self):
        self._action = "delete"
        return self

    # --- WHERE ---
    def where(self, **conditions):
        for k, v in conditions.items():
            if isinstance(v, str):
                v = f"'{v}'"
                o = '='
            elif isinstance(v, (tuple, list)):
                v = f"'{v[1]}'"
                o = f"'{v[0]}'"
            self._where.append(f"{k}{o}{v}")
        return self

    # --- ORDER BY ---
    def order_by(self, column, direction="ASC"):
        self._order_by = f"{column} {direction.upper()}"
        return self

    # --- LIMIT ---
    def limit(self, n: int):
        self._limit = n
        return self

    # --- SQL BUILDER ---
    def SQL(self) -> str:
        if self._action == "insert":
            cols = ", ".join(self._values.keys())
            vals = ", ".join(
                [f"'{v}'" if isinstance(v, str) else str(v) for v in self._values.values()]
            )
            return f"INSERT INTO {self.table} ({cols}) VALUES ({vals});"

        if self._action == "select":
            cols = ", ".join(self._columns)
            sql = f"SELECT {cols} FROM {self.table}"
            if self._where:
                sql += " WHERE " + " AND ".join(self._where)
            if self._order_by:
                sql += f" ORDER BY {self._order_by}"
            if self._limit:
                sql += f" LIMIT {self._limit}"
            return sql + ";"

        if self._action == "update":
            sets = ", ".join(
                [f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in self._values.items()]
            )
            sql = f"UPDATE {self.table} SET {sets}"
            if self._where:
                sql += " WHERE " + " AND ".join(self._where)
            return sql + ";"

        if self._action == "delete":
            sql = f"DELETE FROM {self.table}"
            if self._where:
                sql += " WHERE " + " AND ".join(self._where)
            return sql + ";"

        raise ValueError("No action defined (insert/select/update/delete)")
